def add_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    result = add_numbers(10, 5)
    print(result)