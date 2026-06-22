def sum_two_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    x = 7
    y = 13
    result = sum_two_numbers(x, y)
    print(result)