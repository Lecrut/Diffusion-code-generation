import datetime

def days_in_month(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def days_passed_in_month(date):
    return date.day

def calculate_remaining_days(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    if target_month > current_month:
        target_year = current_year
        target_month_num = target_month
    elif target_month < current_month:
        target_year = current_year - 1
        target_month_num = target_month + 12
    else:
        target_year = current_year
        target_month_num = target_month
    remaining_days = days_in_month(target_year, target_month_num) - days_passed_in_month(current_date)
    return remaining_days
if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    target_month = 5
    print(calculate_remaining_days(sample_date, target_month))