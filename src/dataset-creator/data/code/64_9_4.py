import datetime
from dateutil.relativedelta import relativedelta
def format_localized_datetime(dt_instance: datetime.datetime) -> str:
    if dt_instance.tzinfo is None:
        local_dt = dt_instance.replace(tzinfo=datetime.timezone.utc).astimezone()
    else:
        try:
            utc_offset = int(dt_instance.utcoffset().total_seconds()) / 3600 * -1
            base_tz = datetime.timezone(datetime.timedelta(hours=utc_offset))
            local_dt = dt_instance.astimezone(base_tz)
        except (ValueError, OverflowError):
            local_dt = dt_instance.replace(tzinfo=datetime.timezone.utc).astimezone()
    return local_dt.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_utc = datetime.datetime(2023, 10, 5, 14, 30)
    sample_local_tz = datetime.datetime(2023, 10, 6, 8, 15, tzinfo=datetime.timezone(datetime.timedelta(hours=5)))
    print(format_localized_datetime(sample_utc))
    print(format_localized_datetime(sample_local_tz))