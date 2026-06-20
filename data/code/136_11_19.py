def check_number_ranges(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a non-negative integer")
    
    return (num >= 0 and num < 10) or (num >= 20 and num < 30) or (num >= 40 and num < 50)

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35, 45, 55]
    for case in test_cases:
        try:
            print(f"Number {case}: {check_number_ranges(case)}")
        except ValueError as e:
            print(e)