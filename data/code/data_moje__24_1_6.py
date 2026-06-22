import calendar

def is_leap_year(year: int) -> bool:
    rules = {
        'divisible_by_400': lambda y: y % 400 == 0,
        'divisible_by_100': lambda y: y % 100 == 0,
        'divisible_by_4': lambda y: y % 4 == 0,
        'default': lambda y: False,
    }
    if rules['divisible_by_400'](year):
        return True
    if rules['divisible_by_100'](year):
        return False
    if rules['divisible_by_4'](year):
        return True
    return rules['default'](year)

if __name__ == '__main__':
    test_years = [2024, 1900, 2000]
    for year in test_years:
        result = is_leap_year(year)
        print(result)