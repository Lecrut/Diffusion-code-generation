def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, -1, -2, -3]
    results = {num: is_odd(num) for num in test_values}
    print(results)