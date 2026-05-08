import datetime
def calculate_days_remaining(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    if target_month == today.month:
        if target_day > today.day:
            return (datetime.date(year, today.month, 1) + datetime.timedelta(days=31)) - today
        else:
            return target_day - today.day
    else:
        next_month = today.month + 1
        next_year = year
        if next_month > 12:
            next_month = 1
            next_year += 1
        first_day_of_target_month = datetime.date(year, target_month, 1)
        if target_month == 12:
            last_day_of_target_month = datetime.date(year, 12, 31)
        else:
            last_day_of_target_month = datetime.date(year, target_month + 1, 1) - datetime.timedelta(days=1)
        days_until_end = (last_day_of_target_month - today).days
        if target_month == today.month:
            return (datetime.date(year, target_month, 1) + datetime.timedelta(days=31)) - today
        else:
            return days_until_end
if __name__ == '__main__':
    target_month_1 = 12
    target_day_1 = 31
    result_1 = calculate_days_remaining(target_month_1, target_day_1)
    print(f"Target Month: {target_month_1}, Day: {target_day_1}, Days Remaining: {result_1}")
    target_month_2 = 1
    target_day_2 = 1
    result_2 = calculate_days_remaining(target_month_2, target_day_2)
    print(f"Target Month: {target_month_2}, Day: {target_day_2}, Days Remaining: {result_2}")
    target_month_3 = 6
    target_day_3 = 30
    result_3 = calculate_days_remaining(target_month_3, target_day_3)
    print(f"Target Month: {target_month_3}, Day: {target_day_3}, Days Remaining: {result_3}")