def subtract_numbers(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(10, 5)
    print(result)