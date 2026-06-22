def check_negativity(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0.0, -3.14, 25]
    results = {value: check_negativity(value) for value in sample_values}
    print(results)