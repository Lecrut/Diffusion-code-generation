import datetime
from zoneinfo import ZoneInfo as TZ
def format_localized_date(date_obj: datetime.datetime) -> str:
    return date_obj.strftime("%B %d, %Y") if not date_obj.tzinfo else\
        date_obj.astimezone(TZ("UTC")).strftime("%A, %B %d, %Y at %I:%M%p in %Z (%Z)")
if __name__ == '__main__':
    sample_utc = datetime.datetime(2023, 10, 5, 14, 30)
    sample_pst = datetime.datetime(2023, 10, 6, 7, 30, tzinfo=TZ("America/Los_Angeles"))
    print(f"UTC: {format_localized_date(sample_utc)}")
    print(f"PST: {format_localized_date(sample_pst)}")