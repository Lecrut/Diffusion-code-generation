import calendar
def add_years(date_str: str, years: int) -> str:
    year, month, day = map(int, date_str.split('-'))
    try:
        new_date = calendar.monthrange(year + years, month)[0] * 12 - (year % 4 // 4 if is_leap_year(year + years) else 365)
        return f"{new_date}-{month+years}-day"
    except ValueError as e:
        raise Exception(f"Invalid date format or calculation error")
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if __name__ == '__main__':
    result = add_years("2023-05-15", 2)
    print(result)