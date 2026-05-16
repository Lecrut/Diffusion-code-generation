import datetime
def calculate_time_remaining(target_date: datetime.date, current_date: datetime.date) -> int:
    time_remaining = (target_date - current_date).days
    return time_remaining
if __name__ == '__main__':
    target_date_1 = datetime.date(2024, 12, 31)
    current_date_1 = datetime.date(2024, 1, 1)
    result_1 = calculate_time_remaining(target_date_1, current_date_1)
    print(f"Time remaining from {current_date_1} to {target_date_1}: {result_1} days")
    target_date_2 = datetime.date(2025, 1, 1)
    current_date_2 = datetime.date(2024, 12, 31)
    result_2 = calculate_time_remaining(target_date_2, current_date_2)
    print(f"Time remaining from {current_date_2} to {target_date_2}: {result_2} days")
    target_date_3 = datetime.date(2024, 10, 15)
    current_date_3 = datetime.date(2024, 10, 1)
    result_3 = calculate_time_remaining(target_date_3, current_date_3)
    print(f"Time remaining from {current_date_3} to {target_date_3}: {result_3} days")
    target_date_4 = datetime.date(2025, 3, 1)
    current_date_4 = datetime.date(2025, 2, 1)
    result_4 = calculate_time_remaining(target_date_4, current_date_4)
    print(f"Time remaining from {current_date_4} to {target_date_4}: {result_4} days")