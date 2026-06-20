def check_number_ranges(num):
    return (num >= 0 and num <= 5) or (num >= 10 and num <= 15) or (num >= 20 and num <= 25)

if __name__ == '__main__':
    test_cases = [3, 12, 23, -1, 6]
    results = [check_number_ranges(case) for case in test_cases]
    print(results)