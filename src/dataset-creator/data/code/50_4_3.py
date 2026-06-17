def sum_three(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All inputs must be numeric.")
    return a + b + c
if __name__ == '__main__':
    result = sum_three(10.5, 20, -3)
    print(result)