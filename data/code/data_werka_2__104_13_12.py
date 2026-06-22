import datetime

def validate_date_input(value):
    if not isinstance(value, datetime.date):
        raise ValueError("Input must be a datetime.date instance")
    return value

def get_iso_week_key(date_obj):
    iso_data = date_obj.isocalendar()
    return (iso_data[0], iso_data[1])

def is_same_week(date_a, date_b):
    validated_a = validate_date_input(date_a)
    validated_b = validate_date_input(date_b)
    key_a = get_iso_week_key(validated_a)
    key_b = get_iso_week_key(validated_b)
    return key_a == key_b

if __name__ == '__main__':
    start_of_year = datetime.date(2023, 1, 2)
    end_of_year = datetime.date(2023, 1, 8)
    next_week = datetime.date(2023, 1, 9)
    print(is_same_week(start_of_year, end_of_year))
    print(is_same_week(start_of_year, next_week))