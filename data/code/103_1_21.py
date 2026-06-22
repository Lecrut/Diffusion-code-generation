from calendar import timegm
from datetime import datetime, timezone, timedelta

MILLISECONDS_PER_SECOND = 1000

def get_milliseconds_elapsed_today() -> int:
    now_utc = datetime.now(timezone.utc)
    start_of_day_utc = datetime(now_utc.year, now_utc.month, now_utc.day, 0, 0, 0, tzinfo=timezone.utc)
    timegm_now = timegm(now_utc.timetuple())
    timegm_start = timegm(start_of_day_utc.timetuple())
    seconds_elapsed = timegm_now - timegm_start
    milliseconds = seconds_elapsed * MILLISECONDS_PER_SECOND + now_utc.microsecond // 1000
    return milliseconds

if __name__ == '__main__':
    ms_value = get_milliseconds_elapsed_today()
    print(ms_value)