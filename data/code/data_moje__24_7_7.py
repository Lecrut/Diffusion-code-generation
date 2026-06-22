def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2004]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y}: {result}")