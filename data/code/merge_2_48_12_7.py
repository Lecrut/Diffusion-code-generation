from typing import Union
def calculate_quotient(first_operand: float, second_operand: float) -> float:
    try:
        if not isinstance(first_operand, (int, float)) or not isinstance(second_operand, (int, float)):
            raise TypeError("Both operands must be numeric types.")
        if second_operand == 0.0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_operand / second_operand
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        raise
if __name__ == '__main__':
    sample_first = 10.5
    sample_second = 2
    try:
        result = calculate_quotient(sample_first, sample_second)
        print(result)
    except Exception as e:
        print(f"Error occurred: {e}")