def sum_three_numbers(a: float | int = 0, b: float | int = 1, c: float | int = 2) -> float | int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("All arguments must be integers or floats.")
    return int(a) + int(b) + int(c)
if __name__ == '__main__':
    result = sum_three_numbers(10.5, 20, -3.7)