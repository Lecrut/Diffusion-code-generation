def is_odd(num):
    return num & 1 == 1

if __name__ == '__main__':
    test_values = [5, 10, 15, 20]
    results = {num: is_odd(num) for num in test_values}
    print(results)