def is_leap_year(year):
    is_divisible_by_4 = year & 3 == 0
    is_divisible_by_100 = year % 100 == 0
    is_divisible_by_400 = year % 400 == 0
    return is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)

if __name__ == '__main__':
    test_cases = [2024, 1900, 2000, 2023, 400, 1000]
    for year in test_cases:
        result = is_leap_year(year)
        print(f"Year {year} is a leap year: {result}")