import datetime
import time

_SECONDS_IN_HOUR = 3600
_SECONDS_IN_MINUTE = 60
_SECONDS_IN_DAY = 86400

_UNITS = {
    "hour": _SECONDS_IN_HOUR,
    "minute": _SECONDS_IN_MINUTE,
    "day": _SECONDS_IN_DAY,
    "second": 1,
}

def get_seconds_since_start_of_day() -> int:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    total_seconds = current_hour * _UNITS["hour"] + current_minute * _UNITS["minute"] + current_second * _UNITS["second"]
    return total_seconds

if __name__ == '__main__':
    result = get_seconds_since_start_of_day()
    print(result)