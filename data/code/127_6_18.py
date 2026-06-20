def verify_oddity(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    return num & 1 == 1

if __name__ == '__main__':
    test_values = [2, 3, 5, 8, 10, -3, 0]
    for value in test_values:
        print(f"{value}: {verify_oddity(value)}")