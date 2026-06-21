def check_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    for y in test_years:
        print(check_leap(y))