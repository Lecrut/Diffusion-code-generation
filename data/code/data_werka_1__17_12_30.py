def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, -4, -3, 2, 7]
    results = {value: is_even(value) for value in test_values}
    print(results)