from typing import Union

ADD = "add"
SUBTRACT = "subtract"

def perform_operation(operation: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if operation == ADD:
        return a + b
    elif operation == SUBTRACT:
        return a - b
    else:
        raise ValueError("Invalid operation")

if __name__ == '__main__':
    result_add = perform_operation(ADD, 5, 3)
    result_sub = perform_operation(SUBTRACT, 10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")