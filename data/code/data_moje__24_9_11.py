def check_divisible_by(year, divisor):
    return year % divisor == 0

def determine_leap_status(year):
    is_div_by_four = check_divisible_by(year, 4)
    is_div_by_hundred = check_divisible_by(year, 100)
    is_div_by_four_hundred = check_divisible_by(year, 400)
    
    if is_div_by_four_hundred:
        return True
    if is_div_by_hundred:
        return False
    return is_div_by_four

if __name__ == '__main__':
    test_years = [1996, 2100, 2400, 1800, 2025]
    for y in test_years:
        print(determine_leap_status(y))