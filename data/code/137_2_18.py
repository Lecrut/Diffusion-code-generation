LEAP_YEAR_CONDITION_1 = 4
LEAP_YEAR_CONDITION_2 = 100
LEAP_YEAR_CONDITION_3 = 400

def is_leap_year(year):
    return year % LEAP_YEAR_CONDITION_1 == 0 and year % LEAP_YEAR_CONDITION_2 != 0 or year % LEAP_YEAR_CONDITION_3 == 0
if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2020))
    print(is_leap_year(2021))