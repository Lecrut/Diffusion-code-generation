from datetime import datetime, timedelta

EARLIEST_DATE = datetime.min
LATER_DATE = datetime.max

def determine_earlier_iso_date(first: str, second: str) -> datetime:
    dt_first = datetime.fromisoformat(first)
    dt_second = datetime.fromisoformat(second)
    if dt_first < dt_second:
        return dt_first
    return dt_second

if __name__ == '__main__':
    sample_first = "2023-05-20T10:00:00"
    sample_second = "2023-05-21T10:00:00"
    earlier = determine_earlier_iso_date(sample_first, sample_second)
    print(earlier)