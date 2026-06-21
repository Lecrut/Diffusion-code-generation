def is_positive(number):
    return number > 0

if __name__ == '__main__':
    SAMPLE_VALUES = [15, -20, 0, 7, -3]
    results = {value: is_positive(value) for value in SAMPLE_VALUES}
    print(results)