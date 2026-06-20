from typing import Union

class DivisionCalculator:
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Error: Both inputs must be numbers.'
        if b == 0:
            return 'Error: Division by zero is not allowed.'
        return a / b

if __name__ == '__main__':
    calculator = DivisionCalculator()
    result1 = calculator.divide(10, 2)
    print(result1)
    result2 = calculator.divide(5.5, 0)
    print(result2)