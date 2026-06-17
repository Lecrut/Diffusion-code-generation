from datetime import date
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 2023, 1900]
    for y in sample_years:
        print(f"{y}: {is_leap_year(y)}")