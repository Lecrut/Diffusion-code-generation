import datetime
def calculate_time_remaining(target_date_str, current_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    if target_date < current_date:
        return "Target date is in the past."
    time_difference = target_date - current_date
    if time_difference.days < 0:
        return "Error in calculation."
    return time_difference.days
if __name__ == '__main__':
    target = "2024-03-15"
    current = "2024-02-10"
    result = calculate_time_remaining(target, current)
    print(result)
    target_leap = "2024-03-01"
    current_leap = "2024-02-29"
    result_leap = calculate_time_remaining(target_leap, current_leap)
    print(result_leap)
    target_past = "2023-01-01"
    current_past = "2024-01-01"
    result_past = calculate_time_remaining(target_past, current_past)
    print(result_past)
    target_same = "2024-02-10"
    current_same = "2024-02-10"
    result_same = calculate_time_remaining(target_same, current_same)
    print(result_same)