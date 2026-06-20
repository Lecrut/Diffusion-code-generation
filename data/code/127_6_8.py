def verify_oddity(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n & 1 == 1

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, "a", None]
    for value in test_values:
        try:
            print(f"Value {value}: {verify_oddity(value)}")
        except TypeError as e:
            print(e)