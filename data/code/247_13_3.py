def sum_two_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    try:
        result = sum_two_integers(5, 3)
        print(result)
    except ValueError as e:
        print(e)