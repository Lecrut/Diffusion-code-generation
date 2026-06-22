def add_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers.')
    return a + b
if __name__ == '__main__':
    try:
        result1 = add_numbers(5, 3)
        print(result1)
        result2 = add_numbers(-10, 20)
        print(result2)
        result3 = add_numbers('5', 3)
    except ValueError as e:
        print(e)