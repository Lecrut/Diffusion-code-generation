def is_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, -3.7, 1e-10, -1e-10]
    results = {value: is_zero(value) for value in sample_values}
    print(results)