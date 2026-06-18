import datetime
from zoneinfo import ZoneInfo
def format_full_month(date_obj: datetime.datetime) -> str:
    date_obj = date_obj.astimezone(ZoneInfo("UTC"))
    return date_obj.strftime("%B")
if __name__ == '__main__':
    sample_date = datetime.datetime.now(tz=datetime.timezone.utc)
    result = format_full_month(sample_date)
    print(result)