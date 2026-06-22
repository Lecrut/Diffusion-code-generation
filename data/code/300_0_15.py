import calendar
from datetime import date

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 
    5: 31, 6: 30, 7: 31, 8: 31, 
    9: 30, 10: 31, 11: 30, 12: 31
}

def calculate_remaining_days(current_date):
    month = current_date.month
    year = current_date.year
    days_in_month = DAYS_IN_MONTH[month]
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month == 2:
            days_in_month += 1
    
    return days_in_month - current_date.day

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    remaining_days = calculate_remaining_days(sample_date)
    print(remaining_days)