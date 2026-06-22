from datetime import date, timedelta

TUESDAY_INDEX = 1
REFERENCE_DATE = date(2023, 7, 4)

def validate_date_input(input_date: date) -> date:
    if not isinstance(input_date, date):
        raise ValueError("Input must be a date instance")
    return input_date

def calculate_days_to_next_tuesday(current_date: date) -> int:
    current_weekday = current_date.weekday()
    difference = (TUESDAY_INDEX - current_weekday) % 7
    return 7 if difference == 0 else difference

def get_upcoming_tuesday(reference: date) -> date:
    validated_ref = validate_date_input(reference)
    days_offset = calculate_days_to_next_tuesday(validated_ref)
    return validated_ref + timedelta(days=days_offset)

if __name__ == '__main__':
    start = REFERENCE_DATE
    final_date = get_upcoming_tuesday(start)
    print(final_date)