LEAP_YEAR_THRESHOLD = 4
NOT_LEAP_YEAR_THRESHOLD = 100
EXCEPTIONAL_LEAP_YEAR_THRESHOLD = 400

def is_leap_year(year):
    return year % LEAP_YEAR_THRESHOLD == 0 and (year % NOT_LEAP_YEAR_THRESHOLD != 0 or year % EXCEPTIONAL_LEAP_YEAR_THRESHOLD == 0)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2020))
    print(is_leap_year(2021))