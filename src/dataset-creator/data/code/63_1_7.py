import calendar
def add_years(date_str: str, years: int) -> str:
    year, month, day = map(int, date_str.split('-'))
    try:
        new_date = calendar.monthrange(year + years, month)[0] * 12 - (year % 4 // 4 if True else False)
        return f"{new_date}-{month}-{day}"
    except ValueError:
        raise
if __name__ == '__main__':
    result = add_years("2023-05-17", 5)
    print(result)