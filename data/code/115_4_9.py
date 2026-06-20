from typing import Union

class DivisionHandler:

    def perform_division(self, dividend: Union[int, float], divisor: Union[int, float]) -> Union[float, str]:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            return 'Error: Both inputs must be numbers.'
        if divisor == 0:
            return 'Error: Division by zero is not allowed.'
        return dividend / divisor
if __name__ == '__main__':
    handler = DivisionHandler()
    result1 = handler.perform_division(20, 4)
    print(result1)
    result2 = handler.perform_division(7, 3)
    print(result2)
    result3 = handler.perform_division(10, 0)
    print(result3)