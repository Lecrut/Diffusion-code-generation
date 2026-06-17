import re
def sanitize_input(value: str) -> float | int:
    pattern = r'^[-+]?(\d+(\.\d+)?)$'
    if not re.match(pattern, value.strip()):
        raise ValueError("Invalid numeric input")
    return float(value.strip())
if __name__ == '__main__':
    operand_a_str = "12.5"
    operand_b_str = "-3.7"
    try:
        operand_a = sanitize_input(operand_a_str)
        operand_b = sanitize_input(operand_b_str)
        result = operand_a + operand_b
        print(result)
    except ValueError as e:
        raise RuntimeError(f"Input error: {e}") from None