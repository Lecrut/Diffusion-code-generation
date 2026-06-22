from datetime import datetime
import calendar

def get_next_day(date_str: str) -> datetime:
    year, month, day = date_str.split('-')
    y, m, d = int(year), int(month), int(day)
    days_in_month = calendar.monthrange(y, m)[1]
    if d < days_in_month:
        d += 1
    else:
        d = 1
        if m < 12:
            m += 1
        else:
            m = 1
            y += 1
    return datetime(y, m, d)

if __name__ == '__main__':
    sample_date = '2024-02-28'
    result = get_next_day(sample_date)
    print(result)