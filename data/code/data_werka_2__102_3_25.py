import time

WEEKDAY_THRESHOLD = 5

def validate_weekday_index(index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index > 6:
        raise ValueError("Index must be between 0 and 6")
    return True

def get_current_weekday_index():
    timestamp = time.localtime()
    return timestamp.tm_wday

def is_current_date_weekday():
    index = get_current_weekday_index()
    validate_weekday_index(index)
    return index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    result = is_current_date_weekday()
    print(result)