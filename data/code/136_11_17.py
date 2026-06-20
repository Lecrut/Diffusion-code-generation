def check_number_ranges(num):
    return (num >= 0 and num < 10) or (num >= 20 and num < 30) or (num >= 40 and num < 50)

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35, 45, 55]
    results = {num: check_number_ranges(num) for num in test_cases}
    print(results)