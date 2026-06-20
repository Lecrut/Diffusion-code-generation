from datetime import datetime

def fraction_of_month_remaining():
    now = datetime.now()
    days_in_month = 30 if now.month in {4, 6, 9, 11} else 31
    if now.month == 2:
        days_in_month = 28 + (now.year % 4 == 0 and (now.year % 100 != 0 or now.year % 400 == 0))
    remaining_days = days_in_month - now.day
    return remaining_days / days_in_month

if __name__ == '__main__':
    print(fraction_of_month_remaining())