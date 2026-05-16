import datetime
def calculate_days_remaining(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    if target_month == today.month:
        days_in_month = (datetime.date(year, target_month + 1, 1) - datetime.date(year, target_month, 1)).days
        return days_in_month - target_day
    else:
        next_month = target_month + 1
        if next_month > 12:
            next_month = 1
            year += 1
        first_day_of_next_month = datetime.date(year, next_month, 1)
        current_month_end = datetime.date(year, target_month, 1) + datetime.timedelta(days=31)
        if target_month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, target_month + 1, 1)
        days_in_target_month = (next_month_start - datetime.date(year, target_month, 1)).days
        days_remaining = days_in_target_month - target_day
        return days_remaining
if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    result_1 = calculate_days_remaining(target_month_1, target_day_1)
    print(f"Target Month: {target_month_1}, Day: {target_day_1}")
    print(f"Days remaining until end of month: {result_1}")
    target_month_2 = 12
    target_day_2 = 31
    result_2 = calculate_days_remaining(target_month_2, target_day_2)
    print(f"Target Month: {target_month_2}, Day: {target_day_2}")
    print(f"Days remaining until end of month: {result_2}")
    target_month_3 = 1
    target_day_3 = 1
    result_3 = calculate_days_remaining(target_month_3, target_day_3)
    print(f"Target Month: {target_month_3}, Day: {target_day_3}")
    print(f"Days remaining until end of month: {result_3}")