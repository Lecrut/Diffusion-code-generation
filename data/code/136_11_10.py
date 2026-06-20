def check_number_range(num):
    return (num >= 0 and num <= 10) or (num >= 20 and num <= 30)

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35]
    for case in test_cases:
        print(f"Number {case}: {check_number_range(case)}")