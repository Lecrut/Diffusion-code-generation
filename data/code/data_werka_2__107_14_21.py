from datetime import datetime
from calendar import timegm

INPUT_DATE_FORMAT = '%d-%m-%Y %H:%M:%S'
ISO_8601_SEPARATOR = 'T'
ISO_8601_SUFFIX = ''

def _parse_to_tuple(date_str: str) -> tuple:
    parsed = datetime.strptime(date_str, INPUT_DATE_FORMAT)
    return (
        parsed.year,
        parsed.month,
        parsed.day,
        parsed.hour,
        parsed.minute,
        parsed.second,
        0,
        0,
        -1
    )

def _tuple_to_epoch(time_tuple: tuple) -> int:
    return timegm(time_tuple)

def _epoch_to_iso(epoch_value: int) -> str:
    epoch_dt = datetime.utcfromtimestamp(epoch_value)
    return epoch_dt.strftime('%Y-%m-%d') + ISO_8601_SEPARATOR + epoch_dt.strftime('%H:%M:%S') + ISO_8601_SUFFIX

def convert_date_to_iso(date_string: str) -> str:
    time_tuple = _parse_to_tuple(date_string)
    epoch_seconds = _tuple_to_epoch(time_tuple)
    return _epoch_to_iso(epoch_seconds)

if __name__ == '__main__':
    sample_date = '15-08-2023 09:15:30'
    iso_result = convert_date_to_iso(sample_date)
    print(iso_result)