def is_negative(number):
    return number < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -3.5, 2.3]
    results = {value: is_negative(value) for value in test_values}
    print(results)