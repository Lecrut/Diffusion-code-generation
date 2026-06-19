def is_positive(value):
    return value > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.5, -2.4]
    results = {value: is_positive(value) for value in sample_values}
    print(results)