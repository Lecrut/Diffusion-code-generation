from datetime import date, timedelta

WEEKDAY_SATURDAY = 5

def calculate_upcoming_saturday(start_date: date) -> date:
    current_day_index = start_date.weekday()
    days_remaining_in_week = 7 - current_day_index
    distance_to_target = WEEKDAY_SATURDAY - current_day_index
    if distance_to_target < 0:
        distance_to_target += 7
    return start_date + timedelta(days=distance_to_target)

if __name__ == '__main__':
    fixed_reference = date(2023, 11, 1)
    computed_date = calculate_upcoming_saturday(fixed_reference)
    print(computed_date)