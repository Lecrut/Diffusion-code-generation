def check_even(number):
    if not isinstance(number, int) or isinstance(number, bool):
        return "ERROR: Invalid type"
    return number % 2 == 0

if __name__ == '__main__':
    samples = [4, 7, 10, 3.14, "4", True]
    for value in samples:
        result = check_even(value)
        print(result)