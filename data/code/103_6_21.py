import time
import calendar

_SECONDS_PER_HOUR = 3600
_SECONDS_PER_MINUTE = 60

_UNIT_MULTIPLIERS = {
    'hour': _SECONDS_PER_HOUR,
    'minute': _SECONDS_PER_MINUTE,
    'second': 1,
}

def compute_seconds_elapsed_today():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    seconds_today = (
        local_time.tm_hour * _UNIT_MULTIPLIERS['hour'] +
        local_time.tm_min * _UNIT_MULTIPLIERS['minute'] +
        local_time.tm_sec * _UNIT_MULTIPLIERS['second']
    )
    return seconds_today

if __name__ == '__main__':
    elapsed = compute_seconds_elapsed_today()
    print(elapsed)