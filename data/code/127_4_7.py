def is_odd(number):
    return number % 2 == 1

if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    results = {num: "Odd" if is_odd(num) else "Even" for num in test_numbers}
    print(results)