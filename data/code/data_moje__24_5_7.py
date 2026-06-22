DIVISOR_FOUR = 4
DIVISOR_HUNDRED = 100
DIVISOR_FOUR_HUNDRED = 400

def check_leap(year: int) -> bool:
    is_divisible_by_four = (year % DIVISOR_FOUR == 0)
    is_divisible_by_hundred = (year % DIVISOR_HUNDRED == 0)
    is_divisible_by_four_hundred = (year % DIVISOR_FOUR_HUNDRED == 0)

    if not is_divisible_by_four:
        return False
    if not is_divisible_by_hundred:
        return True
    return is_divisible_by_four_hundred

if __name__ == '__main__':
    sample_years = [2024, 2100, 2400, 2023, 1996]
    for current_year in sample_years:
        result = check_leap(current_year)
        print(result)