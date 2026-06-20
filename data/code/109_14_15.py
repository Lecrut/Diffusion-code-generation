import datetime

def days_until_end_of_month(year, month):
    target_date = datetime.date(year, month, 1)
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    days_left = (next_month_start - target_date).days
    return days_left

if __name__ == '__main__':
    year = 2023
    month = 10
    print(f"Days left until the end of {month}/{year}: {days_until_end_of_month(year, month)}")