def _validate_year_input(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year <= 0:
        raise ValueError("Year must be positive")

def check_leap_status(year):
    _validate_year_input(year)
    divisible_by_four = year % 4 == 0
    divisible_by_hundred = year % 100 == 0
    divisible_by_four_hundred = year % 400 == 0
    if divisible_by_four_hundred:
        return True
    if divisible_by_hundred:
        return False
    return divisible_by_four

if __name__ == '__main__':
    print(check_leap_status(2400))
    print(check_leap_status(1700))
    print(check_leap_status(2024))