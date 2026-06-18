def sum_three(a: int | float, b: int | float, c: int | float) -> int | float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All inputs must be integers or floats.")
    return a + b + c
if __name__ == '__main__':
    result = sum_three(10.5, 20, -3)
    print(result)