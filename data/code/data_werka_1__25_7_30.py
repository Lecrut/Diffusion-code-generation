def is_zero(s):
    try:
        num = float(s)
        return num == 0
    except ValueError:
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", "0e0", "0x0"]
    results = {value: is_zero(value) for value in test_values}
    print(results)