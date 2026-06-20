def check_both_true(a, b):
    return a and b

if __name__ == '__main__':
    result1 = check_both_true(True, True)
    print(f"check_both_true(True, True): {result1}")
    result2 = check_both_true(False, False)
    print(f"check_both_true(False, False): {result2}")