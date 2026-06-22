def is_greater(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a > b

if __name__ == '__main__':
    try:
        print(is_greater(5, 3))
        print(is_greater(2, 4))
        print(is_greater(-1, -3))
        print(is_greater(5, 'a'))
    except ValueError as e:
        print(e)