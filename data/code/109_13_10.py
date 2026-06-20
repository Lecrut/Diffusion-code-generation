import datetime

def days_in_month(year, month):
    if month == 12:
        return 31
    elif month in {1, 3, 5, 7, 8, 10}:
        return 31
    elif month == 2:
        if (year % 4 != 0 or year % 100 != 0) and year % 400 != 0:
            return 28
        else:
            return 29
    else:
        return 30

def days_left_in_month(start_date):
    today = datetime.date.today()
    if start_date.year > today.year or (start_date.year == today.year and start_date.month > today.month):
        raise ValueError("Start date must be in the past or current month")
    end_of_month = datetime.date(today.year, start_date.month, days_in_month(start_date.year, start_date.month))
    return (end_of_month - today).days + 1

if __name__ == '__main__':
    sample_start_date = datetime.date(2023, 10, 15)
    print(days_left_in_month(sample_start_date))