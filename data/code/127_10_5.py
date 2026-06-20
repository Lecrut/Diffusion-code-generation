def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    test_numbers = [2, 3, 5, 8, 10, 17]
    results = {num: is_odd(num) for num in test_numbers}
    print(results)