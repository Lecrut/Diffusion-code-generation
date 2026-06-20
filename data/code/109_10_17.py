import datetime

def calculate_days_remaining():
    today = datetime.date.today()
    current_month_end = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)
    return (current_month_end - today).days

if __name__ == '__main__':
    sample_value = calculate_days_remaining()
    print(sample_value)