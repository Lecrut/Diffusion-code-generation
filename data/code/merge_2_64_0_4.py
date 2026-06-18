import datetime
from zoneinfo import ZoneInfo
def format_full_month(date_obj: datetime.datetime) -> str:
    return date_obj.strftime("%B")
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, tzinfo=ZoneInfo("America/New_York"))
    print(format_full_month(sample_date))