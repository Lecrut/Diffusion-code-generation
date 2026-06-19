def is_strictly_less_than_zero(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [0.0, -0.0, -1e-308, 1e-308, -1.0, 1.0]
    results = {value: is_strictly_less_than_zero(value) for value in sample_values}
    print(results)