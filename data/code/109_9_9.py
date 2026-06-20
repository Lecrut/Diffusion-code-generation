import datetime

def calculate_days_in_current_month():
    today = datetime.date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    return num_days

if __name__ == '__main__':
    days_remaining = calculate_days_in_current_month()
    print(days_remaining)