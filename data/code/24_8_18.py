def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    test_years = [1900, 2000, 2024]
    for y in test_years:
        print(f"{y}: {is_leap_year(y)}")