import sys
def sanitize_input(value: str) -> float | int:
    try:
        return float(value) if '.' in value else int(float(value))
    except ValueError:
        raise TypeError(f"Invalid input type: {value}")
if __name__ == '__main__':
    operand_a = "12.5"
    operand_b = "-30"
    try:
        num_a = sanitize_input(operand_a)
        num_b = sanitize_input(operand_b)
        result = num_a + num_b
        print(result)
    except TypeError as e:
        sys.exit(f"Error: {e}")