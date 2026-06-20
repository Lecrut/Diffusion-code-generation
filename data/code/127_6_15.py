def verify_oddity(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {num: verify_oddity(num) for num in test_values}
    print(results)