from test import Test
import message

class TestInvest(Test):
    def test_under_minimum(self):
        self.command('!create')

        replies = self.command('!invest 50')
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0], message.modify_min_invest(100))

    def test_negative(self):
        self.command('!create')

        replies = self.command('!invest -50')
        self.assertEqual(len(replies), 0)

    def test_non_number(self):
        self.command('!create')

        replies = self.command('!invest abc')
        self.assertEqual(len(replies), 0)

    def test_none(self):
        self.command('!create')

        replies = self.command('!invest')
        self.assertEqual(len(replies), 0)

    def test_insufficient_funds(self):
        self.command('!create')

        replies = self.command('!invest 2000')
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0], message.modify_insuff(1000))

    def test_basic(self):
        self.command('!create')

        replies = self.command('!invest 100')
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0], message.modify_invest(100, 100, 900))

    def test_invest_100_percent(self):
        self.command('!create')

        replies = self.command('!invest 100%')
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0], message.modify_invest(1000, 100, 0))

    def test_invest_50_percent(self):
        self.command('!create')

        replies = self.command('!invest 50%')
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0], message.modify_invest(500, 100, 500))
