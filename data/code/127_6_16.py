def verify_oddity(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number & 1 != 0

if __name__ == '__main__':
    sample_values = [3, 5, 8, 12]
    for value in sample_values:
        print(f"{value} is odd: {verify_oddity(value)}")