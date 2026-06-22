def is_leap_year(year):
    divisible_by_four = year % 4 == 0
    divisible_by_hundred = year % 100 == 0
    divisible_by_four_hundred = year % 400 == 0
    if divisible_by_four_hundred:
        return True
    if divisible_by_hundred:
        return False
    return divisible_by_four

if __name__ == '__main__':
    print(is_leap_year(1600))
    print(is_leap_year(1700))
    print(is_leap_year(2004))
    print(is_leap_year(2100))