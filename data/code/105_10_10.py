from datetime import datetime
import calendar

DAYS_IN_WEEK = 7
MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

def get_next_calendar_day(date_string: str) -> datetime:
    year, month, day = (int(part) for part in date_string.split('-'))
    last_day_of_month = calendar.monthrange(year, month)[1]
    
    if day < last_day_of_month:
        next_day = day + 1
        next_month = month
        next_year = year
    elif month < 12:
        next_day = 1
        next_month = month + 1
        next_year = year
    else:
        next_day = 1
        next_month = 1
        next_year = year + 1
    
    return datetime(year=next_year, month=next_month, day=next_day)

if __name__ == '__main__':
    input_date = '2023-12-31'
    result = get_next_calendar_day(input_date)
    print(result)