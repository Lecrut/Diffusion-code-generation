from datetime import date

def days_left_in_month():
    today = date.today()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    last_day_of_month = date(today.year, today.month, last_day_of_month)
    days_remaining = (last_day_of_month - today).days
    return days_remaining

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 11
    result = days_left_in_month()
    print(result)