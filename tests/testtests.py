from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        uc = Calculator()
        self.assertEquals(6, uc.add(2, 4))
