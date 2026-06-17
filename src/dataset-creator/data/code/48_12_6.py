def calculate_quotient(first_operand: float | int, second_operand: float | int) -> float:
    try:
        first = float(first_operand)
        second = float(second_operand)
        if second == 0:
            raise ValueError("Division by zero is not allowed.")
        return first / second
    except TypeError as e:
        print(f"Input validation error: {e}")
        raise
if __name__ == '__main__':
    result = calculate_quotient(10, 2)
    print(result)