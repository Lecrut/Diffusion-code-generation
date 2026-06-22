def is_strictly_greater(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a > b

if __name__ == '__main__':
    print(is_strictly_greater(10, 5))
    print(is_strictly_greater(20, 30))
    print(is_strictly_greater(7, 7))
    print(is_strictly_greater(-5, 12))
    print(is_strictly_greater(0, -1))