import calendar
from datetime import datetime, timezone

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
SAMPLE_DATA = {
    'epoch': 0,
    'new_year_2021': 1609459200,
    'mid_2023': 1688169600
}

def format_unix_timestamp(unix_ts: int) -> str:
    if not isinstance(unix_ts, (int, float)):
        raise ValueError("Timestamp must be numeric")
    dt_obj = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
    return dt_obj.strftime(TIMESTAMP_FORMAT)

if __name__ == '__main__':
    for name, ts in SAMPLE_DATA.items():
        formatted_date = format_unix_timestamp(ts)
        print(formatted_date)