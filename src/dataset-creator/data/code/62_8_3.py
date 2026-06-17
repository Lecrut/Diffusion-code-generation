from datetime import datetime, timedelta
def add_months(dt: datetime, months: int) -> tuple:
    try:
        year = dt.year + (months // 12)
        month = dt.month - 1 + ((months % 12))
        if month > 0:
            day = min(dt.day, calendar_month_days(year, month))
        else:
            raise ValueError("Invalid date arithmetic")
        new_dt = datetime(year=year, month=int(month), day=int(day))
    except Exception as e:
        print(f"Error adding months: {e}")
        return None, None
    timestamp = new_dt.timestamp()
    if not isinstance(new_dt, datetime) or not isinstance(timestamp, float):
        raise ValueError("Invalid output types")
    return new_dt, timestamp
def calendar_month_days(year: int, month: int) -> int:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if len(months) < int(month):
        raise ValueError("Invalid month")
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return months[int(month)] + 1 if len(months) > int(month) else months[int(month - 1)]
if __name__ == '__main__':
    current_date = datetime.now()
    sample_months_to_add = [3, -2]
    for m in sample_months_to_add:
        new_dt, ts = add_months(current_date, m)
        if new_dt is not None and ts is not None:
            print(f"Original Date: {current_date}")
            print(f"Added Months: {m}")
            print(f"New Datetime: {new_dt}")
            print(f"Timestamp: {ts}\n")
    current_date = datetime(2023, 5, 1)
    sample_months_to_add = [7]
    for m in sample_months_to_add:
        new_dt, ts = add_months(current_date, m)
        if new_dt is not None and ts is not None:
            print(f"Original Date: {current_date}")
            print(f"Added Months: {m}")
            print(f"New Datetime: {new_dt}")
            print(f"Timestamp: {ts}\n")
    try:
        new_dt, ts = add_months(current_date, 13)
        if new_dt is not None and ts is not None:
            print(f"Original Date: {current_date}")
            print(f"Added Months: {m}")
            print(f"New Datetime: {new_dt}")
            print(f"Timestamp: {ts}\n")
    except ValueError as e:
        print(f"Error occurred while processing months: {e}")