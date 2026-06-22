LEAP_DIVISORS = (4, 100, 400)

def check_leap_status(year_value):
    divisible_by_four = year_value % LEAP_DIVISORS[0] == 0
    if not divisible_by_four:
        return False
    divisible_by_hundred = year_value % LEAP_DIVISORS[1] == 0
    if not divisible_by_hundred:
        return True
    return year_value % LEAP_DIVISORS[2] == 0

if __name__ == '__main__':
    sample_inputs = [2000, 1900, 2024, 2023, 1600, 1700]
    for val in sample_inputs:
        print(check_leap_status(val))