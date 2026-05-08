import datetime
if __name__ == '__main__':
    month = 10
    year = 2023
    try:
        target_date = datetime.date(year, month, 1)
        next_month = target_date.replace(day=1) + datetime.timedelta(days=32)
        days_left = (next_month - datetime.date(year, month + 1, 1)).days
        if month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, month + 1, 1)
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        days_left_to_end = days_in_month - (target_date.day - 1)
        print(f"Month: {month}, Year: {year}")
        print(f"Days left until the end of the month: {days_left_to_end}")
    except ValueError as e:
        print(f"Error in date calculation: {e}")