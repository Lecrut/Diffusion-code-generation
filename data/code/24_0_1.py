LEAP_RULES = {
    'divisible_by_400': lambda y: y % 400 == 0,
    'divisible_by_100': lambda y: y % 100 == 0,
    'divisible_by_4': lambda y: y % 4 == 0
}

def is_leap_year(year):
    return LEAP_RULES['divisible_by_400'](year) or (not LEAP_RULES['divisible_by_100'](year) and LEAP_RULES['divisible_by_4'](year))

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))