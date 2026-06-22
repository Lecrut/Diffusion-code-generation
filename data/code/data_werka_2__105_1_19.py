from datetime import date, timedelta

def _validate_date_input(year, month, day):
    try:
        return date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e

def _calculate_days_to_next_sunday(target_date):
    weekday = target_date.weekday()
    days_ahead = 6 - weekday
    if days_ahead == 0:
        return 7
    return days_ahead

def get_first_sunday_after_jan_1_2024():
    base_date = _validate_date_input(2024, 1, 1)
    offset_days = _calculate_days_to_next_sunday(base_date)
    return base_date + timedelta(days=offset_days)

if __name__ == '__main__':
    result = get_first_sunday_after_jan_1_2024()
    print(result)