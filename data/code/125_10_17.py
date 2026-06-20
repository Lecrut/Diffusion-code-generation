from typing import Union

class SimpleArithmetic:
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

    @staticmethod
    def perform_operation(operation: str, a: int, b: int) -> Union[int, float]:
        if operation == SimpleArithmetic.ADD:
            return a + b
        elif operation == SimpleArithmetic.SUBTRACT:
            return a - b
        elif operation == SimpleArithmetic.MULTIPLY:
            return a * b
        elif operation == SimpleArithmetic.DIVIDE:
            if b == 0:
                raise ValueError('Cannot divide by zero')
            return a / b
        else:
            raise ValueError('Unsupported operation')

if __name__ == '__main__':
    calculator = SimpleArithmetic()
    print(calculator.perform_operation(SimpleArithmetic.ADD, 5, 3))
    print(calculator.perform_operation(SimpleArithmetic.SUBTRACT, 10, 4))
    print(calculator.perform_operation(SimpleArithmetic.MULTIPLY, 7, 2))
    try:
        print(calculator.perform_operation(SimpleArithmetic.DIVIDE, 9, 0))
    except ValueError as e:
        print(e)