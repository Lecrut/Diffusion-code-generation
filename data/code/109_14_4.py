import datetime
if __name__ == '__main__':
    month = 10
    year = 2023
    try:
        target_date = datetime.date(year, month, 1)
        next_month = target_date.replace(day=1) + datetime.timedelta(days=32)
        days_left = (next_month - datetime.date(year, month + 1, 1)).days
        if month == 12:
            days_left = 0
        else:
            days_left = (datetime.date(year, month + 1, 1) - target_date).days - 1
        print(f"The number of days left until the end of {month}/{year} is: {days_left}")
    except ValueError:
        print("Invalid month or year provided.")