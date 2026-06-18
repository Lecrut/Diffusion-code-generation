def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 2004, 2100, 2023]
    for y in sample_years:
        result = is_leap_year(y)
        print(f"{y} is {'a' if result else 'not a'} leap year.")