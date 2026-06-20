from typing import Union

class DivisionHandler:
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Error: Both inputs must be numbers.'
        if b == 0:
            return 'Error: Division by zero is not allowed.'
        return a / b

if __name__ == '__main__':
    handler = DivisionHandler()
    result1 = handler.divide(10, 2)
    print(result1)
    result2 = handler.divide(7.5, 3)
    print(result2)
    result3 = handler.divide(5, 0)
    print(result3)