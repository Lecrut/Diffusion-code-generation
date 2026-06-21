def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    years = [2000, 1900, 2024]
    for y in years:
        print(is_leap_year(y))