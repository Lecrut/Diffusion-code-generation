def check_number_ranges(number):
    return (number >= 0 and number <= 50) or (number >= 100 and number <= 200)

if __name__ == '__main__':
    test_cases = [30, 75, 150, 250]
    for case in test_cases:
        print(f"Number {case}: {check_number_ranges(case)}")