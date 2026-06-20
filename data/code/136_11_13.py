def check_number_ranges(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be an integer or float")
    
    return (num >= 0 and num < 10) or (num >= 20 and num < 30) or (num >= 40 and num < 50)

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35, 45, 55]
    for case in test_cases:
        try:
            result = check_number_ranges(case)
            print(f"Number {case}: {result}")
        except ValueError as e:
            print(e)