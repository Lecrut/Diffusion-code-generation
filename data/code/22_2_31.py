def is_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_values = {17: True, 42: False, -3: True, 0: False}
    for value in test_values:
        result = is_odd(value)
        print(f"Is {value} odd? {result}")