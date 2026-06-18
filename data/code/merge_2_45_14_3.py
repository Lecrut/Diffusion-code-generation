import sys
def sanitize_input(value: str) -> float | int:
    try:
        return float(value) if '.' in value else int(float(value))
    except ValueError:
        raise TypeError(f"Invalid input type '{value}'. Only numeric values are allowed.") from None
if __name__ == '__main__':
    operand_a = sanitize_input("42")
    operand_b = sanitize_input("-17.5")
    result = operand_a + operand_b
    print(result)