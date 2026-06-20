from typing import Union

class DivisionHandler:
    def divide(self, dividend: Union[int, float], divisor: Union[int, float]) -> Union[float, str]:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            return 'Error: Both inputs must be numbers.'
        if divisor == 0:
            return 'Error: Division by zero is not allowed.'
        return dividend / divisor

if __name__ == '__main__':
    calculator = DivisionHandler()
    result1 = calculator.divide(10, 2)
    print(result1)
    result2 = calculator.divide(5.5, 3)
    print(result2)
    result3 = calculator.divide(7, 0)
    print(result3)