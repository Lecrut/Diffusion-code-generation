def check_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    test_values = {42: True, -10: False, 100: False, 3.14: False}
    for value, expected in test_values.items():
        result = check_number(value)
        print(f"{value}: {result} (Expected: {expected})")