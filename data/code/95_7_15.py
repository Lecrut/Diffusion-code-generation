def validate_attributes(a, b, c):
    checks = {
        'a_positive': a > 0,
        'b_even': b % 2 == 0,
        'c_divisible_by_a': a != 0 and c % a == 0
    }
    return all(checks.values())

if __name__ == '__main__':
    print(f"Test 1 (a=2, b=4, c=6): {validate_attributes(2, 4, 6)}")
    print(f"Test 2 (a=3, b=5, c=7): {validate_attributes(3, 5, 7)}")
    print(f"Test 3 (a=-1, b=2, c=4): {validate_attributes(-1, 2, 4)}")
    print(f"Test 4 (a=2, b=3, c=5): {validate_attributes(2, 3, 5)}")
    print(f"Test 5 (a=5, b=4, c=10): {validate_attributes(5, 4, 10)}")
    print(f"Test 6 (a=1, b=2, c=5): {validate_attributes(1, 2, 5)}")
    print(f"Test 7 (a=1, b=3, c=5): {validate_attributes(1, 3, 5)}")