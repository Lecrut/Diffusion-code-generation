def is_leap_year(year):
    return (year % 400 == 0) and (year % 100 != 0) or year % 4 == 0
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    for y in test_years:
        print(f"{y}: {is_leap_year(y)}")