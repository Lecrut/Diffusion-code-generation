from datetime import datetime, timedelta

FRIDAY_INDEX = 4
REFERENCE_DATE = datetime(2023, 12, 15)

def validate_date_input(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object")
    return date_obj

def calculate_days_to_next_friday(reference_date):
    current_weekday = reference_date.weekday()
    days_offset = FRIDAY_INDEX - current_weekday
    if days_offset <= 0:
        days_offset += 7
    return days_offset

def get_upcoming_friday(reference_date):
    validated_date = validate_date_input(reference_date)
    days_to_add = calculate_days_to_next_friday(validated_date)
    return validated_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    ref_date = REFERENCE_DATE
    result = get_upcoming_friday(ref_date)
    print(result.strftime("%Y-%m-%d"))