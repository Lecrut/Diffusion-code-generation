def is_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = [0, -0.0, 1e-308, 1, -1]
    results = {value: is_zero(value) for value in test_values}
    print(results)