import datetime

def validate_date(date_obj):
    if not isinstance(date_obj, datetime.datetime):
        raise ValueError("Input must be a datetime object")

def fractional_day_to_seconds(fractional_day):
    return fractional_day * 24 * 60 * 60

def calculate_elapsed_time(date_obj):
    validate_date(date_obj)
    now = datetime.datetime.now()
    time_difference = now - date_obj
    return fractional_day_to_seconds(time_difference.total_seconds())

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 1, 1, 10, 0, 0)
    elapsed_time = calculate_elapsed_time(sample_date)
    print(elapsed_time)