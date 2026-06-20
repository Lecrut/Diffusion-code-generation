def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_numbers = [2, 3, 4, 5]
    results = {num: is_even(num) for num in test_numbers}
    print(results)