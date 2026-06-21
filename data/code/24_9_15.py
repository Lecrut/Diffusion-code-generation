DIVISOR_FOUR = 4
DIVISOR_HUNDRED = 100
DIVISOR_FOUR_HUNDRED = 400

def is_leap_year(year):
    if year % DIVISOR_FOUR_HUNDRED == 0:
        return True
    if year % DIVISOR_HUNDRED == 0:
        return False
    if year % DIVISOR_FOUR == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2400))
    print(is_leap_year(1800))
    print(is_leap_year(2024))
    print(is_leap_year(2025))