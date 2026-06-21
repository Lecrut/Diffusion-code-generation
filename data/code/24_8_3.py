def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == '__main__':
    test_years = [2024, 1900, 2000]
    for y in test_years:
        print(is_leap_year(y))