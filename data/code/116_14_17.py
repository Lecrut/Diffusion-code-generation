def sum_three(a: int, b: int, c: int) -> int:
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All arguments must be integers")
    return a + b + c

if __name__ == '__main__':
    result = sum_three(10, 20, 30)
    print(result)