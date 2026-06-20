from datetime import date

def days_left_in_month():
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    return num_days - today.day + 1
if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    days_remaining = days_left_in_month()
    print(days_remaining)