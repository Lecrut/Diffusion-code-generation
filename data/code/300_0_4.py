from datetime import date

def days_remaining_in_month(current_date):
    _, month, year = current_date.year, current_date.month, current_date.year
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    last_day_of_current_month = date(next_month[0], next_month[1], 1) - timedelta(days=1)
    return (last_day_of_current_month - current_date).days

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(days_remaining_in_month(sample_date))