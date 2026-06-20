def verify_oddity(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    return num & 1 == 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, -1, -2, -3]
    for value in sample_values:
        print(f"Number {value}: {verify_oddity(value)}")