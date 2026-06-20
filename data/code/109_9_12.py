import datetime
DAYS_IN_MONTH = 30

def calculate_remaining_days_in_month(current_date):
    current_year, current_month = (current_date.year, current_date.month)
    if current_month == 12:
        next_month_start = datetime.date(current_year + 1, 1, 1)
    else:
        next_month_start = datetime.date(current_year, current_month + 1, 1)
    return (next_month_start - current_date).days
if __name__ == '__main__':
    current_date = datetime.date(2024, 6, 15)
    remaining_days = calculate_remaining_days_in_month(current_date)
    print(remaining_days)