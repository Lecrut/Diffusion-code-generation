def verify_oddity(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number & 1 == 1

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, -1, 0]
    for value in sample_values:
        print(f"Number {value}: {verify_oddity(value)}")