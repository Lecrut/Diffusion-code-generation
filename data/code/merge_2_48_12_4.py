def calculate_quotient(first_operand: float | int, second_operand: float | int) -> float:
    try:
        first_float = float(first_operand)
        second_float = float(second_operand)
        return first_float / second_float
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid input or division by zero.")
if __name__ == '__main__':
    result = calculate_quotient(10.5, 2)
    print(result)