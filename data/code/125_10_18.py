from typing import Union
ADDITION = 'add'
SUBTRACTION = 'subtract'
MULTIPLICATION = 'multiply'
DIVISION = 'divide'

def perform_operation(operation: str, a: int, b: int) -> Union[int, float]:
    if operation == ADDITION:
        return a + b
    elif operation == SUBTRACTION:
        return a - b
    elif operation == MULTIPLICATION:
        return a * b
    elif operation == DIVISION:
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    print(perform_operation(ADDITION, 5, 3))
    print(perform_operation(SUBTRACTION, 10, 4))
    print(perform_operation(MULTIPLICATION, 7, 2))
    try:
        print(perform_operation(DIVISION, 9, 0))
    except ValueError as e:
        print(e)