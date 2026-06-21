def check_evenness(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, -2, -3, 4, 5, 100, -100]
    for value in sample_values:
        print(f"{value}: {check_evenness(value)}")