def is_odd(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    return num & 1 == 1

if __name__ == '__main__':
    test_values = [7, 23, 45, 68]
    results = {num: is_odd(num) for num in test_values}
    print(results)