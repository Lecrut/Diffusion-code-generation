def analyze_number(n):
    if n <= 0:
        return False, False, False
    if n % 6 == 0:
        return True, True, True
    if n % 2 == 0:
        return True, True, False
    if n % 3 == 0:
        return True, False, True
    return True, False, False

if __name__ == '__main__':
    test_values = [18, 7, -2, 12, 9]
    for val in test_values:
        result = analyze_number(val)
        print(f"{val}: {result}")