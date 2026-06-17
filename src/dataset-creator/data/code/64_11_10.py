import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date: datetime.datetime) -> str:
    return date.strftime("%B %d, %Y") if not date.tzinfo else date.astimezone(ZoneInfo("America/New_York")).strftime("%A, %B %d, %Y at %I:%M%p in America/New_York")
if __name__ == '__main__':
    sample_naive = datetime.datetime(2023, 10, 5, 14, 30)
    sample_tz_aware = datetime.datetime(2023, 10, 6, 8, 45, tzinfo=datetime.timezone(datetime.timedelta(hours=5)))
    print(format_localized_date(sample_naive))
    print(format_localized_date(sample_tz_aware))