def is_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = [1, 0, -5, 100, 0.0, -0.0]
    for value in test_values:
        print(f"Is {value} zero? {is_zero(value)}")