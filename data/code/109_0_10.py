from datetime import datetime, timedelta

def days_remaining_in_month():
    today = datetime.now()
    _, last_day = calendar.monthrange(today.year, today.month)
    end_of_month = datetime(today.year, today.month, last_day)
    return (end_of_month - today).days + 1

if __name__ == '__main__':
    print(days_remaining_in_month())