def check_number_ranges(number):
    return (number >= 0 and number <= 5) or (number >= 10 and number <= 15) or (number >= 20 and number <= 25)

if __name__ == '__main__':
    test_cases = [3, 12, 23, -1, 6]
    results = [check_number_ranges(case) for case in test_cases]
    print(results)