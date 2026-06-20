import datetime

def get_last_day_of_month(date):
    if date.month == 12:
        return date.replace(year=date.year + 1, month=1) - datetime.timedelta(days=1)
    else:
        return date.replace(month=date.month + 1, day=1) - datetime.timedelta(days=1)

def calculate_days_remaining_in_current_month(current_date):
    last_day_of_current_month = get_last_day_of_month(current_date)
    days_remaining = (last_day_of_current_month - current_date).days
    return days_remaining

if __name__ == '__main__':
    current_date = datetime.date(2024, 3, 15)
    if not isinstance(current_date, datetime.date):
        print("Invalid date format.")
    else:
        result = calculate_days_remaining_in_current_month(current_date)
        print(f"Days remaining in the current month: {result}")