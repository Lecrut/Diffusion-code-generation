import datetime
def add_months_to_date(current_datetime: datetime.datetime, months_delta: int) -> tuple[datetime.datetime, float]:
    if not isinstance(current_datetime, datetime.datetime):
        raise TypeError("The first argument must be a datetime instance.")
    if not isinstance(months_delta, int):
        raise TypeError("The second argument must be an integer representing months to add.")
    year = current_datetime.year + (months_delta // 12)
    month = current_datetime.month - 1 + ((months_delta % 12))
    if month <= 0:
        month += 12
    day = min(current_datetime.day, datetime.date(year, month, 1).day)
    new_datetime = current_datetime.replace(year=year, month=month, day=day)
    return (new_datetime, new_datetime.timestamp())
if __name__ == '__main__':
    sample_date = datetime.datetime.now()
    months_to_add = 3
    result_datetime, result_timestamp = add_months_to_date(sample_date, months_to_add)
    print(f"Original Date: {sample_date}")
    print(f"Months to Add: {months_to_add}")
    print(f"New DateTime Object: {result_datetime}")
    print(f"Timestamp Value: {result_timestamp}")