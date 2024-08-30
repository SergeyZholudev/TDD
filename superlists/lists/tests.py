from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    '''тест на токсичность'''

    def test_bad_maths(self):
        '''тест: направильные математические рассчёты'''
        self.assertEqual(1 + 2, 3)
