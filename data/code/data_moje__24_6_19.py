def check_leap_year(year):
    is_divisible_by_4 = (year & 3) == 0
    if not is_divisible_by_4:
        return False
    is_divisible_by_100 = (year % 100) == 0
    if not is_divisible_by_100:
        return True
    is_divisible_by_400 = (year % 400) == 0
    return is_divisible_by_400

if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, 2400, 1700, 1600]
    for y in sample_years:
        result = check_leap_year(y)
        print(f"{y}: {result}")