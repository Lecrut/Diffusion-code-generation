def calculate_quotient(first_operand: float | int, second_operand: float | int) -> float:
    try:
        return first_operand / second_operand
    except ZeroDivisionError as e:
        raise ValueError("Second operand cannot be zero.") from e
if __name__ == '__main__':
    result = calculate_quotient(10, 2)
    print(result)