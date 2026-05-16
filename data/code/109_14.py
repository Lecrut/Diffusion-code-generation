import datetime
if __name__ == '__main__':
    month = 10
    year = 2023
    try:
        target_date = datetime.date(year, month, 1)
        next_month = target_date.replace(day=1) + datetime.timedelta(days=32)
        days_left = (next_month - datetime.date(year, month + 1, 1)).days
        if month == 12:
            days_in_month = 31
        else:
            days_in_month = 30 if month % 12 != 1 else 28
        if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
            if month == 2:
                days_in_month = 29
        days_remaining = days_in_month - target_date.day
        print(f"Month: {month}, Year: {year}")
        print(f"Days left until the end of the month: {days_remaining}")
    except ValueError as e:
        print(f"Error in date calculation: {e}")