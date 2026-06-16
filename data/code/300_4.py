import argparse
def calculate_remaining_days(month, year):
    import datetime
    today = datetime.date.today()
    first_day_of_month = datetime.date(year, month, 1)
    if today.year == year and today.month == month:
        days_in_month = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 28
    else:
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    days_remaining = days_in_month - (today.day - 1)
    return days_remaining
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('month', type=int, nargs='?', default=6, help='The month (1-12)')
    parser.add_argument('year', type=int, nargs='?', default=2023, help='The year')
    args = parser.parse_args()
    month_val = args.month
    year_val = args.year
    remaining = calculate_remaining_days(month_val, year_val)
    print(f"Remaining days in {month_val}/{year_val}: {remaining}")