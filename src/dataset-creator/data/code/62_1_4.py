from datetime import date, timedelta
def add_months(d: date, months: int) -> date:
    year = d.year + (months // 12)
    month = d.month - 1 + ((months % 12))
    if month > 11 or month < 0:
        raise ValueError("Invalid number of months")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 1 and year % 4 == 0:
        days_in_month[2] = 29
    day_of_year = d.timetuple().tm_yday + (months // 12) * 365.25
    while True:
        new_day = min(day_of_year, len(days_in_month)) - 1
        if month == 0 or month >= 12:
            day = days_in_month[month]
            if d.day > day and (months % 12 != 0):
                year += months // 12 + 1
                new_day -= len(days_in_month) * ((years - old_year))
        else:
            break
    return date(year, month + 1, min(d.day, days_in_month[month]))
if __name__ == '__main__':
    today = date.today()
    result_date = add_months(today, 3)
    print(result_date.strftime("%Y-%m-%d"))