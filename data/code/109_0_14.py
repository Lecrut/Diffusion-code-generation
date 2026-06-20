import datetime

def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def days_remaining_in_month(year, month):
    today = datetime.date.today()
    if year < today.year or (year == today.year and month < today.month):
        return 0
    elif year == today.year and month == today.month:
        return days_in_month(year, month) - today.day
    else:
        return days_in_month(year, month)

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 10
    remaining_days = days_remaining_in_month(sample_year, sample_month)
    print(remaining_days)