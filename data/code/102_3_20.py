import time

WEEKDAY_THRESHOLD = 5

def validate_weekday_index(index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index > 6:
        raise ValueError("Index out of range")
    return True

def get_current_weekday_index():
    current_time = time.localtime()
    return current_time.tm_wday

def is_current_date_a_weekday():
    weekday_index = get_current_weekday_index()
    validate_weekday_index(weekday_index)
    return weekday_index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    result = is_current_date_a_weekday()
    print(result)