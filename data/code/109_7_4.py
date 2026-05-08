import datetime
def calculate_time_remaining(target_date_str, current_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    if target_date < current_date:
        return "Target date has already passed."
    time_difference = target_date - current_date
    if time_difference.days <= 0:
        return "The target date is today or in the past."
    return str(time_difference.days)
if __name__ == '__main__':
    target = "2024-03-15"
    current = "2024-02-10"
    result1 = calculate_time_remaining(target, current)
    print(f"Time remaining from {current} to {target}: {result1} days")
    target2 = "2025-01-01"
    current2 = "2024-12-31"
    result2 = calculate_time_remaining(target2, current2)
    print(f"Time remaining from {current2} to {target2}: {result2} days")
    target3 = "2024-03-01"
    current3 = "2024-02-29"
    result3 = calculate_time_remaining(target3, current3)
    print(f"Time remaining from {current3} to {target3}: {result3} days")
    target4 = "2024-03-15"
    current4 = "2024-03-15"
    result4 = calculate_time_remaining(target4, current4)
    print(f"Time remaining from {current4} to {target4}: {result4} days")
    target5 = "2023-01-01"
    current5 = "2024-01-01"
    result5 = calculate_time_remaining(target5, current5)
    print(f"Time remaining from {current5} to {target5}: {result5} days")