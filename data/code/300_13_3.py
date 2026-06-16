import datetime
if __name__ == '__main__':
    year = 2023
    month = 12
    days_in_month = 31
    days_passed = datetime.date(year, month, 1).day
    days_remaining = days_in_month - days_passed
    print(days_remaining)