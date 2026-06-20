def check_number_ranges(number):
    return (number >= 0 and number <= 5) or (number >= 10 and number <= 15) or (number >= 20 and number <= 25)

if __name__ == '__main__':
    test_numbers = [3, 12, 23, -1, 6]
    results = {num: check_number_ranges(num) for num in test_numbers}
    print(results)