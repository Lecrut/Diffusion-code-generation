from datetime import datetime

EPOCH_YEAR = 1970
EPOCH_DAY = 1
EPOCH_MONTH = 1
EPOCH_HOUR = 0
EPOCH_MINUTE = 0
EPOCH_SECOND = 0

def is_earlier(first: datetime, second: datetime) -> bool:
    if not isinstance(first, datetime):
        raise ValueError("First argument must be a datetime object")
    if not isinstance(second, datetime):
        raise ValueError("Second argument must be a datetime object")
    epoch = datetime(EPOCH_YEAR, EPOCH_MONTH, EPOCH_DAY, EPOCH_HOUR, EPOCH_MINUTE, EPOCH_SECOND)
    first_seconds = (first - epoch).total_seconds()
    second_seconds = (second - epoch).total_seconds()
    return first_seconds < second_seconds

if __name__ == '__main__':
    date_first = datetime(2024, 1, 1, 0, 0, 0)
    date_second = datetime(2024, 1, 1, 0, 0, 1)
    is_earlier_result = is_earlier(date_first, date_second)
    print(is_earlier_result)