from datetime import datetime

def days_remaining_in_month():
    today = datetime.now()
    end_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
    return (end_of_month - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())