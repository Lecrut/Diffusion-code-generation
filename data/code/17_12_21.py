def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, -1, -2, 3, 4, 5]
    results = {value: is_even(value) for value in test_values}
    print(results)