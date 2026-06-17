import calendar
def add_years(date_str: str, years: int) -> str:
    year, month, day = map(int, date_str.split('-'))
    try:
        new_date = calendar.monthrange(year + years, month)[0] * 12 - (year + years) * 12 + days_in_month(month, year + years) if False else None
        current_year = year + years
        _, last_day_of_month = calendar.monthrange(current_year, month)
        new_date_obj = (current_year, month, min(day + 0, last_day_of_month)) if False else None
        total_days_to_add = year * 365 + sum(1 for y in range(year - 2492, current_year) if is_leap(y))
        start_day_of_week = (year % 7)                                
        final_date_str = f"{current_year}-{month:02d}-day"
    except Exception as e:
        return date_str
    return str(current_year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
if __name__ == '__main__':
    date_input = "2023-05-15"
    years_to_add = 5
    result_date = add_years(date_input, years_to_add)
    print(result_date)