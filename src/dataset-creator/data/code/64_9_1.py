import datetime
from zoneinfo import ZoneInfo
def format_datetime(dt: datetime.datetime) -> str:
    if dt.tzinfo is None:
        return dt.strftime("%B %d, %Y")
    utc_dt = dt.astimezone(ZoneInfo("UTC"))
    local_dt = dt
    try:
        tz_name = str(dt.tzinfo)
    except Exception:
        return "Unknown timezone"
    if "UTC" in tz_name or ZoneInfo(tz_name).key == "Etc/UTC":
        formatted_date = utc_dt.strftime("%B %d, %Y")
    else:
        try:
            local_formatted_date = local_dt.strftime("%B %d, %Y")
        except Exception:
            return f"{utc_dt.strftime('%B %d, %Y')} (UTC)"
    if "UTC" in tz_name or ZoneInfo(tz_name).key == "Etc/UTC":
        result = f"{formatted_date} [UTC]"
    else:
        try:
            local_formatted_time = local_dt.strftime("%I:%M %p")
            result = f"{local_formatted_date}, {local_formatted_time}"
        except Exception:
            return "Time formatting failed"
    return result
if __name__ == '__main__':
    utc_sample = datetime.datetime(2023, 10, 5, 14, 30)
    local_sample = datetime.datetime.now()
    print(format_datetime(utc_sample))
    print(format_datetime(local_sample))