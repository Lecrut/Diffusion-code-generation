def check_number_ranges(num):
    ranges = {
        '0-10': (num >= 0 and num < 10),
        '20-30': (num >= 20 and num < 30),
        '40-50': (num >= 40 and num < 50)
    }
    return any(ranges.values())

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35, 45, 55]
    for case in test_cases:
        print(f"Number {case}: {check_number_ranges(case)}")