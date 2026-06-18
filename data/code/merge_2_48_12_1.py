def calculate_quotient(first_operand: float | int, second_operand: float | int) -> float:
    try:
        return first_operand / second_operand
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero.") from e
    except TypeError as e:
        raise ValueError(f"Invalid operand types. {e}")
if __name__ == '__main__':
    result = calculate_quotient(10, 2)
    print(result)