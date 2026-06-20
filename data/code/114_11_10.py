def multiply_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(4, 3)
    print(result)