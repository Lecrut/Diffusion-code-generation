import re
def sanitize_input(value: str) -> float | int:
    if not isinstance(value, (int, float)):
        cleaned = value.strip()
        match = re.match(r'^[-+]?(\d+(\.\d+)?)$', cleaned)
        if not match:
            raise ValueError("Invalid numeric input")
        return float(cleaned)
def add_operands(a: int | float, b: int | float) -> float:
    result = a + b
    return result
if __name__ == '__main__':
    operand_a_str = "10.5"
    operand_b_str = "-3.2"
    try:
        operand_a = sanitize_input(operand_a_str)
        operand_b = sanitize_input(operand_b_str)
        final_result = add_operands(operand_a, operand_b)
        print(final_result)
    except ValueError as e:
        raise RuntimeError(f"Input error: {e}")