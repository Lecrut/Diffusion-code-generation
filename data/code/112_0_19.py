def add_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    try:
        result = add_numbers(15, 27)
        print(result)
    except ValueError as e:
        print(e)