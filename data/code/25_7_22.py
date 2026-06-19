def is_zero(value):
    try:
        number = float(value)
        return number == 0
    except ValueError:
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "abc", "123", "0x0"]
    results = {value: is_zero(value) for value in test_values}
    print(results)