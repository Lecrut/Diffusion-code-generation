def is_odd(number):
    return number % 2 == 1

if __name__ == '__main__':
    test_numbers = [4, 7, 10, 13]
    results = {num: "Odd" if is_odd(num) else "Even" for num in test_numbers}
    print(results)