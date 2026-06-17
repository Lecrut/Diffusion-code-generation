import datetime
from dateutil.relativedelta import relativedelta
def format_datetime_localized(dt_instance: datetime.datetime) -> str:
    tz = dt_instance.tzinfo
    utc_dt = None
    local_dt = None
    if isinstance(tz, type(datetime.timezone.utc)):
        utc_dt = dt_instance.astimezone()
    try:
        local_dt = dt_instance.replace(tzinfo=datetime.datetime.now().astimezone()).replace(microsecond=0)
    except Exception:
        pass
    formatted_str = dt_instance.strftime("%B %d, %Y")
    return formatted_str
def main():
    sample_utc_dt = datetime.datetime(2023, 10, 5, 14, 30) + datetime.timedelta(hours=7)                                                                                                   
    import pytz
    utc_tz = pytz.UTC
    sample_utc_dt_aware = pytz.utc.localize(datetime.datetime(2023, 10, 5, 14, 30))
    local_sample_naive = datetime.datetime(2023, 9, 28)            
    result_utc = format_datetime_localized(sample_utc_dt_aware).replace("October", "Oct")                                      
    sample_utc = datetime.datetime(2023, 10, 5, 14, 30)
    tz_aware_utc = pytz.UTC.localize(sample_utc)
    local_sample_naive = datetime.datetime(2023, 9, 28, 10, 0)            
    print(f"UTC: {format_datetime_localized(tz_aware_utc)}")
    print(f"Local (Naive): {format_datetime_localized(local_sample_naive)}")
if __name__ == '__main__':
    main()