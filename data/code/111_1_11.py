import datetime

DATE_CONSTANT = datetime.date(2024, 7, 4)
DAYS_TO_ADD = 30

def compute_future_date(anchor: datetime.date, offset: int) -> str:
    if not isinstance(offset, int):
        raise ValueError("Offset must be an integer")
    if anchor.year < 1 or anchor.year > 9999:
        raise ValueError("Invalid year")
    if offset < 0:
        raise ValueError("Offset must be positive")
    target = anchor + datetime.timedelta(days=offset)
    return target.isoformat()

if __name__ == '__main__':
    result = compute_future_date(DATE_CONSTANT, DAYS_TO_ADD)
    print(result)