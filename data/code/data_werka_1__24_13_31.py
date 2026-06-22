def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.14, 7]
    results = {value: is_negative(value) for value in sample_values}
    print(results)