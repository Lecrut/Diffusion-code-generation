def add_two_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers')
    return a + b
if __name__ == '__main__':
    try:
        result1 = add_two_numbers(5.5, 4.5)
        print(result1)
    except ValueError as e:
        print(e)
    try:
        result2 = add_two_numbers(-3.2, 7.8)
        print(result2)
    except ValueError as e:
        print(e)
    try:
        result3 = add_two_numbers('5', 10)
        print(result3)
    except ValueError as e:
        print(e)