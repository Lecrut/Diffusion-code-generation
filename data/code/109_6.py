import datetime
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
    try:
        target_date = datetime.date(target_year, target_month_num, 1)
        if target_month_num == current_month:
            return 0
        if target_month_num == 12:
            next_month_start = datetime.date(target_year + 1, 1, 1)
        else:
            next_month_start = datetime.date(target_year, target_month_num + 1, 1)
        days_in_current_month = (datetime.date(current_year, current_month + 1, 1) - datetime.date(current_year, current_month, 1)).days
        days_passed = (datetime.date(current_year, current_month, 1) - datetime.date(current_year, 1, 1)).days + (target_month_num - 1) * 31                                  
        days_in_current_month_total = (datetime.date(current_year, current_month + 1, 1) - datetime.date(current_year, current_month, 1)).days
        if target_month == current_month:
            return 0
        if target_month > current_month:
            days_until_target = (datetime.date(current_year, current_month + 1, 1) - current_date).days
            return days_until_target
        else:
            return 0
    except ValueError:
        return -1
if __name__ == '__main__':
    current_date_obj = datetime.date(2023, 10, 15)
    target_month_num_1 = 12
    target_month_num_2 = 10
    target_month_num_3 = 11
    print(f"Current Date: {current_date_obj}")
    print(f"Target Month: {target_month_num_1}")
    result1 = calculate_remaining_days(current_date_obj, target_month_num_1)
    print(f"Remaining days in current month until end of target month: {result1}")
    print(f"\nCurrent Date: {current_date_obj}")
    print(f"Target Month: {target_month_num_2}")
    result2 = calculate_remaining_days(current_date_obj, target_month_num_2)
    print(f"Remaining days in current month until end of target month: {result2}")
    print(f"\nCurrent Date: {current_date_obj}")
    print(f"Target Month: {target_month_num_3}")
    result3 = calculate_remaining_days(current_date_obj, target_month_num_3)
    print(f"Remaining days in current month until end of target month: {result3}")