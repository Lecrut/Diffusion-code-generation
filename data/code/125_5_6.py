from typing import Union

class Calculator:
    ADD = "add"
    SUBTRACT = "subtract"

    @staticmethod
    def perform_operation(operation: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if operation == Calculator.ADD:
            return a + b
        elif operation == Calculator.SUBTRACT:
            return a - b
        else:
            raise ValueError("Invalid operation")

if __name__ == '__main__':
    result_add = Calculator.perform_operation(Calculator.ADD, 5, 3)
    result_sub = Calculator.perform_operation(Calculator.SUBTRACT, 10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")