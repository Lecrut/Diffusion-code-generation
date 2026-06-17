import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> dict:
    try:
        dt1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        delta_days = (dt2 - dt1).days
        if delta_days < 0:
            return {"calendar_days": abs(delta_days), "business_days": abs(_count_business_days(dt1, dt2))}
        business_count = _count_business_days(dt1, dt2)
        return {
            "start_date": date1_str,
            "end_date": date2_str,
            "calendar_days": delta_days + 1,
            "business_days": business_count
        }
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
def _count_business_days(start_dt: datetime.datetime, end_dt: datetime.datetime) -> int:
    count = 0
    current_date = start_dt.date()
    while current_date <= end_dt.date():
        if not (current_date.weekday() >= 5):
            count += 1
        current_date += datetime.timedelta(days=1)
    return count
if __name__ == '__main__':
    result = calculate_days_between("2023-10-01", "2023-10-31")
    print(result)