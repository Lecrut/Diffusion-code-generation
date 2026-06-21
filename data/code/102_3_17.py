import time

def get_current_weekday_status(reference_date=None):
    if reference_date is None:
        reference_date = time.localtime()
    if not isinstance(reference_date, time.struct_time):
        raise ValueError("reference_date must be a time.struct_time instance")
    day_index = reference_date.tm_wday
    is_weekday = day_index < 5
    return is_weekday

if __name__ == '__main__':
    current_date = time.localtime()
    result = get_current_weekday_status(current_date)
    print(result)