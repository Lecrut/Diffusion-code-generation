def is_negative(number):
    return number < 0

if __name__ == '__main__':
    test_values = [-5.0, 3.14, 0]
    results = [is_negative(value) for value in test_values]
    print(results)