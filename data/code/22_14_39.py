def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_values = [-10, -5, 0, 5, 10, 15]
    for value in test_values:
        result = is_odd(value)
        print(f"Is {value} odd? {result}")