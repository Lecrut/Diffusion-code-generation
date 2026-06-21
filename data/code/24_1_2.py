def is_leap_year(year):
    is_divisible_by_four = year % 4 == 0
    is_divisible_by_hundred = year % 100 == 0
    is_divisible_by_four_hundred = year % 400 == 0
    
    if is_divisible_by_four_hundred:
        return True
    if is_divisible_by_hundred:
        return False
    if is_divisible_by_four:
        return True
    return False

if __name__ == '__main__':
    test_cases = [2020, 2100, 2400]
    for current_year in test_cases:
        result = is_leap_year(current_year)
        print(result)