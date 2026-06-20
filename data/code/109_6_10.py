import datetime

def calculate_remaining_fraction(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    months_in_year = 12
    
    if target_month > current_month:
        target_year = current_year
        target_month_num = target_month
    elif target_month < current_month:
        target_year = current_year - 1
        target_month_num = target_month + months_in_year
    else:
        target_year = current_year
        target_month_num = target_month
    
    days_in_current_month = (current_date.replace(day=28) + datetime.timedelta(days=4)).day
    days_in_target_month = (datetime.date(target_year, target_month_num, 1).replace(day=28) + datetime.timedelta(days=4)).day
    
    if current_month == target_month:
        return 0.0
    
    remaining_days = days_in_current_month - current_date.day
    total_days = days_in_target_month
    
    fraction_remaining = remaining_days / total_days
    return fraction_remaining

if __name__ == '__main__':
    current_date = datetime.date(2023, 10, 15)
    target_month = 12
    print(calculate_remaining_fraction(current_date, target_month))