from datetime import datetime, timedelta

def is_valid_date(date):
    try:
        datetime.strptime(str(date), '%Y-%m-%d')
        return True
    except ValueError:
        return False

def month_after(date):
    if not is_valid_date(date):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    return date.replace(day=1, month=date.month + 1) + timedelta(days=32) - timedelta(days=(date.replace(day=1, month=date.month + 1) - date).days)

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(month_after(sample_date))