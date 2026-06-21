def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, 2004, 1800, 400, 300]
    for y in sample_years:
        print(is_leap_year(y))