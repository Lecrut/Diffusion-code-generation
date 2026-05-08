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
    target_date = datetime.date(target_year, target_month_num, 1)
    if target_month_num == current_month:
        return 0
    if current_month == 12:
        next_month_start = datetime.date(current_year + 1, 1, 1)
    else:
        next_month_start = datetime.date(current_year, current_month + 1, 1)
    if target_month_num == 12:
        next_month_start_target = datetime.date(target_year + 1, 1, 1)
    else:
        next_month_start_target = datetime.date(target_year, target_month_num + 1, 1)
    last_day_of_target_month = next_month_start_target - datetime.timedelta(days=1)
    if current_month == 12:
        last_day_of_current_month = datetime.date(current_year, 12, 31)
    else:
        last_day_of_current_month = datetime.date(current_year, current_month + 1, 1) - datetime.timedelta(days=1)
    if target_month == current_month:
        return (datetime.date(current_year, current_month, 31) - current_date).days
    end_of_current_month = datetime.date(current_year, current_month, 1) + datetime.timedelta(days=31)                                                         
    if current_month == 12:
        end_of_current_month = datetime.date(current_year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        end_of_current_month = datetime.date(current_year, current_month + 1, 1) - datetime.timedelta(days=1)
    end_of_target_month = datetime.date(target_year, target_month_num, 1) + datetime.timedelta(days=31)                
    if target_month_num == 12:
        end_of_target_month = datetime.date(target_year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        end_of_target_month = datetime.date(target_year, target_month_num + 1, 1) - datetime.timedelta(days=1)
    days_in_current_month = (datetime.date(current_year, current_month + 1, 1) - datetime.date(current_year, current_month, 1)).days
    if target_month == current_month:
        return (datetime.date(current_year, current_month + 1, 1) - current_date).days
    else:
        return (datetime.date(current_year, current_month + 1, 1) - current_date).days
if __name__ == '__main__':
    current_date_sample = datetime.date(2023, 10, 15)
    target_month_sample = 12
    result = calculate_remaining_days(current_date_sample, target_month_sample)
    print(result)
    current_date_sample_2 = datetime.date(2024, 1, 1)
    target_month_sample_2 = 3
    result_2 = calculate_remaining_days(current_date_sample_2, target_month_sample_2)
    print(result_2)