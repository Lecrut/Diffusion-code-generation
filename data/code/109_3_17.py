from datetime import date, timedelta

def days_left_in_month():
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    return num_days - today.day + 1
if __name__ == '__main__':
    test_date = date(2023, 4, 5)
    print(days_left_in_month())