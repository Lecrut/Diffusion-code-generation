def is_negative(value):
    return value < 0

if __name__ == '__main__':
    SAMPLE_VALUES = [10, -5, 0, -3.14, 2.71]
    results = {value: is_negative(value) for value in SAMPLE_VALUES}
    print(results)