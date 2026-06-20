def check_number_ranges(number):
    return (number >= 0 and number <= 50) or \
           (number > 100 and number <= 200) or \
           (number > 300 and number <= 400)

if __name__ == '__main__':
    test_cases = [25, 150, 350, -10, 500]
    for case in test_cases:
        print(f"Number {case}: {check_number_ranges(case)}")