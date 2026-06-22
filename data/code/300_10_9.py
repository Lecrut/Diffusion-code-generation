from datetime import date

def days_remaining_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    last_day_of_current_month = date(year, month, 1) + timedelta(days=31)
    first_day_of_next_month = date(next_month[0], next_month[1], 1)
    return (first_day_of_next_month - last_day_of_current_month).days
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))