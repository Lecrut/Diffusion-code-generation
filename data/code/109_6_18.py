import datetime
DAYS_IN_YEAR = 365

def days_in_month(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_remaining_fraction(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    if target_month > current_month:
        target_year = current_year
    elif target_month < current_month:
        target_year = current_year - 1
    else:
        target_year = current_year
    month_length = days_in_month(target_year, target_month)
    remaining_days = month_length - (current_date.day - 1)
    return remaining_days / month_length
if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    target_month = 6
    fraction_remaining = calculate_remaining_fraction(sample_date, target_month)
    print(fraction_remaining)