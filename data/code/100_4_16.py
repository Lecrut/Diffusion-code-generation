def is_greater(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both inputs must be integers.")
    return x > y

if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(2, 4))