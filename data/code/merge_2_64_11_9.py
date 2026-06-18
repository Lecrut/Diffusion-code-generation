import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        tz = date_obj.tzinfo or ZoneInfo("UTC")
        formatted = date_obj.strftime("%B %d, %Y")
        return f"{formatted} {date_obj.tzname(tz)}"
    except Exception:
        if not date_obj.tzinfo:
            tz_name = "UTC"
        else:
            try:
                from datetime import timezone
                offset = date_obj.utcoffset()
                hours, rest = divmod(offset.total_seconds(), 3600)
                sign = '+' if hours >= 0 else '-'
                abs_hours = int(hours) % 24
                minutes = int(rest / 60)
                tz_name = f"{sign}{abs_hours:02d}:{minutes:02d}"
            except Exception:
                return date_obj.isoformat()
if __name__ == '__main__':
    sample_utc = datetime.datetime(2023, 10, 5, 14, 30)
    sample_eastern = datetime.datetime(2023, 10, 5, 9, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=-4)))
    print(format_localized_date(sample_utc))
    print(format_localized_date(sample_eastern))