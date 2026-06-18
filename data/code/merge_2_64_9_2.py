import datetime
from zoneinfo import ZoneInfo
def format_datetime_localized(dt: datetime.datetime) -> str:
    if dt.tzinfo is None:
        return dt.strftime("%B %d, %Y")
    utc_dt = dt.astimezone(ZoneInfo("UTC"))
    local_tz_name = "Local Time"
    try:
        local_time_str = datetime.datetime.now().strftime("%Z")
        if not local_time_str.endswith("+00"):
            local_tz_name = f"{local_time_str} (Local)"
    except Exception:
        pass
    utc_formatted = utc_dt.strftime(f"%B %d, %Y {utc_dt.hour}:{utc_dt.minute}")
    return f"UTC: {utc_formatted}\n{local_tz_name}: {dt.astimezone().strftime('%A, %B %d, %Y at %I:%M%p')}"
if __name__ == '__main__':
    sample_utc = datetime.datetime(2023, 10, 5, 14, 30)
    sample_local = datetime.datetime.now()
    print(format_datetime_localized(sample_utc))
    print("---")
    print(format_datetime_localized(sample_local))