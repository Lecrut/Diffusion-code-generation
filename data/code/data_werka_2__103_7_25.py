import datetime

DAY_START_HOUR = 0
DAY_START_MINUTE = 0
DAY_START_SECOND = 0
DAY_START_MICROSECOND = 0

def get_elapsed_seconds_since_midnight(reference_time=None):
    if reference_time is None:
        now = datetime.datetime.now()
    else:
        if not isinstance(reference_time, datetime.datetime):
            raise ValueError("reference_time must be a datetime object")
        now = reference_time
    
    if now.hour < DAY_START_HOUR or (now.hour == DAY_START_HOUR and now.minute < DAY_START_MINUTE) or (now.hour == DAY_START_HOUR and now.minute == DAY_START_MINUTE and now.second < DAY_START_SECOND) or (now.hour == DAY_START_HOUR and now.minute == DAY_START_MINUTE and now.second == DAY_START_SECOND and now.microsecond < DAY_START_MICROSECOND):
        raise ValueError("Reference time is before the start of its day")
        
    start_of_day = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
    delta = now - start_of_day
    return delta.total_seconds()

def format_elapsed_time(total_seconds):
    hours = int(total_seconds) // 3600
    remainder = int(total_seconds) % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    result = get_elapsed_seconds_since_midnight()
    formatted = format_elapsed_time(result)
    print(formatted)