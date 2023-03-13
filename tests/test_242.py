# def test_sum ():
#     assert  2 + 2 == 4i
import pytest

from app.calc import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiplication_succesfull(self):
        assert self.calc.addition(self, 2, 2) == 4

    def test_multiplication_unsuccesfull(self):
        assert self.calc.multiplication(self, 2, 2) == 5

    def test_division_succesfull(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_division_unsuccesfull(self):
        assert self.calc.division(self, 4, 2) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_substruction_succesfull(self):
        assert self.calc.substraction(self, 1, 1) == 0

    def test_substruction_unsuccesfull(self):
        assert self.calc.substraction(self, 1, 1) == 1

    def test_addition_successfull(self):
        assert self.calc.addition(self, 1, 1) == 2

    def test_addition_unsuccesfull(self):
        assert self.calc.addition(self, 1, 1) == 3

    def teardown(self):
        print("Выполнен метод Teardown")
