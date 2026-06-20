def check_number_ranges(num):
    return (num >= 0 and num <= 50) or (num >= 100 and num <= 200)

if __name__ == '__main__':
    test_cases = [30, 75, 150, 250]
    for case in test_cases:
        print(f"Number {case}: {check_number_ranges(case)}")