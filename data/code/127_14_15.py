def is_odd(n):
    return n & 1

if __name__ == '__main__':
    test_values = [4, 5, 0, 7, 100]
    results = {num: is_odd(num) for num in test_values}
    print(results)