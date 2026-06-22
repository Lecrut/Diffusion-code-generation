def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_cases = [0, 1, -1, 2, -2, 3, -3, 100, -100]
    results = {num: is_even(num) for num in test_cases}
    print(results)