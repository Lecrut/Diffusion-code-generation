def is_strictly_less_than_zero(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [3.14, -2.718, 0.0, -0.001, 1e-10, -1e-10]
    results = {value: is_strictly_less_than_zero(value) for value in sample_values}
    print(results)