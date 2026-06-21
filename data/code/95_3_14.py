def validate_number(n):
    if n <= 0:
        return False
    if n >= 100:
        return False
    if n % 2 != 0:
        return False
    return True

if __name__ == '__main__':
    result = validate_number(42)
    print(result)
    result2 = validate_number(101)
    print(result2)
    result3 = validate_number(-10)
    print(result3)
    result4 = validate_number(3)
    print(result4)