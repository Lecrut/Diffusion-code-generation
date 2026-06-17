def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
if __name__ == '__main__':
    test_years = [2000, 2023, 1900, 2024]
    for year in test_years:
        print(f"{year}: {'Leap' if is_leap_year(year) else 'Not Leap'}")