import datetime
import time

SECONDS_IN_DAY = 86400

def calculate_fractional_day_seconds(year, month, day, hour, minute, second, microsecond=0):
    current_dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    start_of_day = current_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_seconds = (current_dt - start_of_day).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_dt = datetime.datetime.now()
    result = calculate_fractional_day_seconds(
        sample_dt.year,
        sample_dt.month,
        sample_dt.day,
        sample_dt.hour,
        sample_dt.minute,
        sample_dt.second,
        sample_dt.microsecond
    )
    print(result)