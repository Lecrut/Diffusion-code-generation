import datetime
def calculate_remaining_days(target_month, target_year):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    if target_year == current_year and target_month > current_month:
        remaining_months = 12 - target_month + (target_year % 4 == 0) * 1
        return remaining_months * 30                                                                          
    try:
        target_date = datetime.date(target_year, target_month, 1)
        today = datetime.date.today()
        if target_year == today.year and target_month > today.month:
            days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
            remaining_days = (31 - target_month) * 30 + (31 - target_month)                                           
            if target_year == today.year:
                days_in_target_month = (datetime.date(target_year, 12, 31) - datetime.date(target_year, target_month, 1)).days
                return days_in_target_month + (datetime.date.today() - datetime.date(today.year, today.month, 1)).days                                                                 
            first_of_next_month = datetime.date(target_year, target_month + 1, 1)
            if target_month == 12:
                first_of_next_month = datetime.date(target_year + 1, 1, 1)
            days_in_target_month = (first_of_next_month - target_date).days
            return days_in_target_month
        elif target_year > today.year:
            years_to_add = target_year - today.year
            total_days = years_to_add * 365 + (years_to_add // 4)
            days_remaining_current_year = (datetime.date(today.year + 1, 1, 1) - today).days
            days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
            return days_in_target_month
        else:                                                
             days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
             return days_in_target_month
    except ValueError:
        return "Invalid date"
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)