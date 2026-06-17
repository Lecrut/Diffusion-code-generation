def sum_three(a: int | float, b: int | float, c: int | float) -> int | float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError("All inputs must be integers or floats.")
    return sum([a, b, c])
if __name__ == '__main__':
    result = sum_three(10, 20.5, -3)
    print(result)