def is_odd(num):
    return num & 1 == 1

if __name__ == '__main__':
    test_numbers = [5, 9, 22, 37]
    results = {num: is_odd(num) for num in test_numbers}
    print(results)