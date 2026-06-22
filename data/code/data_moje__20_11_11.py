def check_evenness(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

if __name__ == '__main__':
    samples = [-2, -1, 0, 1, 2, 100, -100]
    for val in samples:
        result = check_evenness(val)
        print(result)