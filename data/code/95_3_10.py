def validate_number(n):
    if n <= 0:
        return False
    if n % 2 != 0:
        return False
    return n < 100

if __name__ == '__main__':
    test_val = 42
    result = validate_number(test_val)
    print(result)