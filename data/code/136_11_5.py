def check_number_ranges(number):
    return (number >= 0 and number <= 10) or \
           (number >= 20 and number <= 30) or \
           (number >= 40 and number <= 50)

if __name__ == '__main__':
    test_cases = [5, 15, 25, 35, 45, 55]
    results = {num: check_number_ranges(num) for num in test_cases}
    print(results)