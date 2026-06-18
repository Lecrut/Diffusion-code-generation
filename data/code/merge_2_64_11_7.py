import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    if date_obj.tzinfo is not None:
        return date_obj.astimezone(ZoneInfo("America/New_York")).strftime("%B %d, %Y")
    else:
        return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_localized_date(sample_date))