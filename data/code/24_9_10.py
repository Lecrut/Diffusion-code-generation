LEAP_DIVISOR_4 = 4
LEAP_DIVISOR_100 = 100
LEAP_DIVISOR_400 = 400

def is_leap_year(year):
    if year % LEAP_DIVISOR_400 == 0:
        return True
    if year % LEAP_DIVISOR_100 == 0:
        return False
    return year % LEAP_DIVISOR_4 == 0

if __name__ == '__main__':
    print(is_leap_year(2400))
    print(is_leap_year(2300))
    print(is_leap_year(2404))
    print(is_leap_year(2401))
    print(is_leap_year(1600))
    print(is_leap_year(1700))