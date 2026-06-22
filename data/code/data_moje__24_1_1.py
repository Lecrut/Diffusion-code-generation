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
    years = [2000, 1900, 2023]
    for y in years:
        print(is_leap_year(y))