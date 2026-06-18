def is_positive(result):
    if result > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    test_cases = [10, -5, 0]
    for case in test_cases:
        print(f"{case}: {is_positive(case)}")