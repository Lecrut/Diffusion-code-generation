import datetime
def calculate_time_remaining(target_date_str, current_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    if target_date < current_date:
        return "Target date has passed."
    if target_date.month == current_date.month:
        days_remaining = (target_date - current_date).days
        return f"Days remaining in the current month: {days_remaining}"
    else:
        if current_date.month == 12:
            next_month = current_date.replace(year=current_date.year + 1, month=1, day=1)
        else:
            next_month = current_date.replace(month=current_date.month + 1, day=1)
        last_day_of_current_month = next_month - datetime.timedelta(days=1)
        days_in_current_month = (last_day_of_current_month - current_date).days + 1
        days_left_in_current_month = (datetime.date(current_date.year, current_date.month, 1) + datetime.timedelta(days=days_in_current_month - 1)) - current_date
        days_until_month_end = (datetime.date(current_date.year, current_date.month, 1) + datetime.timedelta(days=days_in_current_month)) - current_date
        days_in_target_month = (target_date - datetime.date(target_date.year, target_date.month, 1)).days
        total_days_remaining = days_in_target_month
        return f"Time remaining until {target_date.strftime('%Y-%m-%d')}: {total_days_remaining} days."
if __name__ == '__main__':
    target = "2024-03-15"
    current = "2024-01-10"
    print(calculate_time_remaining(target, current))
    target_rollover = "2025-01-05"
    current_rollover = "2024-12-20"
    print(calculate_time_remaining(target_rollover, current_rollover))
    target_same_month = "2024-02-10"
    current_same_month = "2024-02-01"
    print(calculate_time_remaining(target_same_month, current_same_month))
    target_past = "2023-12-01"
    current_past = "2024-01-01"
    print(calculate_time_remaining(target_past, current_past))