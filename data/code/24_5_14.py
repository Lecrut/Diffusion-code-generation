def check_leap(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2100, 2400]
    for year in test_years:
        result = check_leap(year)
        print(f"{year}: {result}")