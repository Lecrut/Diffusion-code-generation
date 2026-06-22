import calendar

def days_left_in_month():
    today = datetime.date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    days_passed = (today.day - 1) if today.day > 1 else 0
    return num_days - days_passed

if __name__ == '__main__':
    sample_day = 5
    sample_month = 4
    sample_year = 2023
    result = days_left_in_month()
    print(result)