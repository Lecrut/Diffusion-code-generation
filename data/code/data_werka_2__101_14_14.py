from datetime import date
import calendar

def calculate_weekday(target_year: int, target_month: int, target_day: int) -> str:
    specified_date = date(year=target_year, month=target_month, day=target_day)
    weekday_numeric = specified_date.weekday()
    weekday_name = calendar.day_name[weekday_numeric]
    return weekday_name

if __name__ == '__main__':
    year_input = 2025
    month_input = 3
    day_input = 15
    computed_result = calculate_weekday(year_input, month_input, day_input)
    print(computed_result)