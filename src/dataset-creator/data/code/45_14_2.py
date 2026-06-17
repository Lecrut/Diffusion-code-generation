import sys
def add(a: float | int = 0, b: float | int = 0) -> float | int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be integers or floats.")
    return a + b
if __name__ == '__main__':
    operand_a = 10.5
    operand_b = 20
    result = add(operand_a, operand_b)
    print(result)