import datetime
from dateutil.relativedelta import relativedelta
def subtract_years_from_date(date_obj: datetime.date, years_to_subtract: int) -> str:
    new_date = date_obj - relativedelta(years=years_to_subtract)
    iso_format = new_date.isoformat() + "Z"
    return iso_format
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        datetime.datetime(2024, 6, 15, 14, 30, 0).replace(tzinfo=datetime.timezone.utc) if hasattr(datetime.datetime, 'tzinfo') else datetime.datetime(2024, 6, 15, 14, 30),
    ]
    results = []
    if hasattr(sample_dates[0], 'replace'):
        d1 = datetime.datetime(2023, 10, 5).replace(tzinfo=datetime.timezone.utc)
        result_1 = subtract_years_from_date(d1.date(), -4)
        results.append(result_1)
    d2_str = "2024-06-15T14:30:00Z"
    try:
        from datetime import timedelta, timezone
        dt_obj = datetime.datetime.strptime(d2_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        result_2 = subtract_years_from_date(dt_obj.date(), -15)
        results.append(result_2)
    except Exception:
        pass
    print(results[0] if len(results) > 0 else "No valid dates processed")