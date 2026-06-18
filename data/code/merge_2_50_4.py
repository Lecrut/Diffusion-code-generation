def sum_three(a: int, b: int, c: int) -> int:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All inputs must be numbers.")
    return a + b + c
if __name__ == '__main__':
    result = sum_three(10, 20.5, -3)
    print(result)