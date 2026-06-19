def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-1, 0, 2.5, -3.7, 10]
    results = [is_negative(val) for val in sample_values]
    print(results)