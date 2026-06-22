def is_greater(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    return a > b

if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(2, 4))
    print(is_greater(-1, -3))