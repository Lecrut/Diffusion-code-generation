from datetime import datetime

def days_remaining_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    
    last_day_of_current_month = datetime(year, month, 1).replace(day=31) + timedelta(days=-1)
    first_day_of_next_month = datetime(next_month[0], next_month[1], 1)
    
    return (first_day_of_next_month - last_day_of_current_month).days

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    print(days_remaining_in_month(sample_year, sample_month))