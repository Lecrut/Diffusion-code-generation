class LeapYearChecker:
    LEAP_YEAR_RULES = {
        'divisible_by_4': lambda year: year % 4 == 0,
        'not_divisible_by_100': lambda year: year % 100 != 0,
        'divisible_by_400': lambda year: year % 400 == 0
    }

    @staticmethod
    def is_leap_year(year):
        return (LeapYearChecker.LEAP_YEAR_RULES['divisible_by_4'](year) and 
                LeapYearChecker.LEAP_YEAR_RULES['not_divisible_by_100'](year)) or \
               LeapYearChecker.LEAP_YEAR_RULES['divisible_by_400'](year)

if __name__ == '__main__':
    print(LeapYearChecker.is_leap_year(2000))
    print(LeapYearChecker.is_leap_year(1900))
    print(LeapYearChecker.is_leap_year(2020))
    print(LeapYearChecker.is_leap_year(2021))