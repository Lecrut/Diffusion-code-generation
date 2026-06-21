from datetime import date

def is_leap_year(year):
    return date(year, 2, 29).month == 2
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2400, 1800]
    for y in test_years:
        print(is_leap_year(y))