from datetime import date, timedelta

def remaining_hours_in_month(year=2023, month=10):
    today = date(year, month, 1)
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    
    remaining_days = (next_month - today).days
    return remaining_days * 24

if __name__ == '__main__':
    print(remaining_hours_in_month())