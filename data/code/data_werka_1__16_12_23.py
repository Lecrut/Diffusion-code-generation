def is_positive(value):
    return value > 0

if __name__ == '__main__':
    sample_values = [0, -1, 2.5, -3.6, 100]
    results = {value: is_positive(value) for value in sample_values}
    print(results)