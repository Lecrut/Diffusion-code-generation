import sys
def add(a: float | int = 0, b: float | int = 0) -> float | int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be integers or floats.")
    return a + b
if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 20
    result = add(sample_a, sample_b)
    print(result)