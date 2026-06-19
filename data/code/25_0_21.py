def is_exactly_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 0.0, 1e-10, -1e-10]
    results = {value: is_exactly_zero(value) for value in sample_values}
    print(results)