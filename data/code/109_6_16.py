import datetime

def calculate_remaining_fraction(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    if target_month > current_month:
        target_year = current_year
    else:
        target_year = current_year - 1
    
    days_in_current_month = (current_date.replace(day=28) + datetime.timedelta(days=4)).day
    days_passed_in_current_month = current_date.day
    days_in_target_month = (datetime.date(target_year, target_month, 1).replace(day=28) + datetime.timedelta(days=4)).day
    
    if current_month == target_month:
        remaining_fraction = 0.0
    else:
        remaining_fraction = (days_in_target_month - 1) / days_in_target_month
    
    return remaining_fraction

if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    target_month = 6
    print(calculate_remaining_fraction(sample_date, target_month))