def is_even(n):
    result = (n & 1) == 0
    return result

if __name__ == '__main__':
    test_values = [10, -5, 3, 8, -2, 7]
    for value in test_values:
        print(f"Is {value} even? {is_even(value)}")