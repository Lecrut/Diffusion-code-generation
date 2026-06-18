from typing import Union
def calculate_quotient(a: float, b: float) -> float:
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numbers.")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    operand_a = 15.0
    operand_b = 3.0
    result = calculate_quotient(operand_a, operand_b)
    print(result)