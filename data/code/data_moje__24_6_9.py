def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == '__main__':
    years = [2000, 1900, 2024, 2023, 2004, 1600, 1700, 2100]
    for y in years:
        result = is_leap_year(y)
        print(f"{y}: {result}")