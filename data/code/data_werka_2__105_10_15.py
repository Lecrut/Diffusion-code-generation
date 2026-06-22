from datetime import datetime
import calendar

def get_next_day(date_str: str) -> datetime:
    year_part, month_part, day_part = date_str.split('-')
    year = int(year_part)
    month = int(month_part)
    day = int(day_part)
    last_day_of_month = calendar.monthrange(year, month)[1]
    if day < last_day_of_month:
        new_day = day + 1
        new_month = month
        new_year = year
    elif month < 12:
        new_day = 1
        new_month = month + 1
        new_year = year
    else:
        new_day = 1
        new_month = 1
        new_year = year + 1
    return datetime(year=new_year, month=new_month, day=new_day)

if __name__ == '__main__':
    input_date = '2000-02-28'
    computed_next = get_next_day(input_date)
    print(computed_next)