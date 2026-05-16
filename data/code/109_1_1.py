import datetime
def time_remaining_in_month(target_month, target_year):
    today = datetime.date.today()
    if target_year == today.year and target_month > today.month:
        target_date = datetime.date(target_year, target_month, 1)
    elif target_year == today.year and target_month < today.month:
        target_date = datetime.date(target_year, target_month, 1)
    elif target_year > today.year:
        target_date = datetime.date(target_year, target_month, 1)
    else:
        target_date = datetime.date(target_year, target_month, 1)
    first_day_of_next_month = datetime.date(target_year, target_month + 1, 1) if target_month < 12 else datetime.date(target_year + 1, 1, 1)
    end_of_month = first_day_of_next_month - datetime.timedelta(days=1)
    if target_date > today:
        remaining_days = (end_of_month - today).days
    else:
        remaining_days = (end_of_month - today).days
    return remaining_days
if __name__ == '__main__':
    target_month_1 = 12
    target_year_1 = 2023
    result_1 = time_remaining_in_month(target_month_1, target_year_1)
    print(f"Target: {target_month_1}/{target_year_1}, Remaining days: {result_1}")
    target_month_2 = 1
    target_year_2 = 2024
    result_2 = time_remaining_in_month(target_month_2, target_year_2)
    print(f"Target: {target_month_2}/{target_year_2}, Remaining days: {result_2}")
    target_month_3 = 6
    target_year_3 = 2024
    result_3 = time_remaining_in_month(target_month_3, target_year_3)
    print(f"Target: {target_month_3}/{target_year_3}, Remaining days: {result_3}")