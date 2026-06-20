def is_odd(num):
    return num & 1 == 1
if __name__ == '__main__':
    test_values = [3, 5, 8, 9]
    results = {num: is_odd(num) for num in test_values}
    print(results)