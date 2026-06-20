import datetime

def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_days_remaining(current_year, current_month):
    today = datetime.date.today()
    if current_year == today.year and current_month == today.month:
        remaining_days = days_in_month(current_year, current_month) - today.day
        return remaining_days
    elif current_year < today.year or (current_year == today.year and current_month < today.month):
        return 0
    else:
        days_till_end_of_current_month = days_in_month(today.year, today.month) - today.day
        days_from_start_of_next_month = sum(days_in_month(year, month) for year in range(today.year + 1, current_year) for month in range(1, 13))
        days_in_remaining_months = sum(days_in_month(current_year, month) for month in range(today.month + 1, current_month))
        return days_till_end_of_current_month + days_from_start_of_next_month + days_in_remaining_months

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 12
    days_left = calculate_days_remaining(sample_year, sample_month)
    print(days_left)