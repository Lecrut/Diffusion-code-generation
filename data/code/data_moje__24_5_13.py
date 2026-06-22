DIVISOR_FOUR = 4
DIVISOR_HUNDRED = 100
DIVISOR_FOUR_HUNDRED = 400

def check_leap(year):
    is_div_four = (year % DIVISOR_FOUR == 0)
    is_div_hundred = (year % DIVISOR_HUNDRED == 0)
    is_div_four_hundred = (year % DIVISOR_FOUR_HUNDRED == 0)
    return (is_div_four and not is_div_hundred) or is_div_four_hundred

if __name__ == '__main__':
    sample_years = [2024, 1900, 2000, 2023, 2100]
    for y in sample_years:
        result = check_leap(y)
        print(result)