from typing import Union
def calculate_quotient(first_operand: float, second_operand: float) -> float:
    try:
        if not isinstance(first_operand, (int, float)) or not isinstance(second_operand, (int, float)):
            raise TypeError("Both operands must be numeric.")
        if second_operand == 0.0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_operand / second_operand
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
if __name__ == '__main__':
    operand_a = 15.0
    operand_b = 3.0
    result = calculate_quotient(operand_a, operand_b)
    print(result)