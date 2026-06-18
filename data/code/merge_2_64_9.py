import datetime
from dateutil import parser as dt_parser
def format_datetime_localized(dt_instance: datetime.datetime) -> str:
    if not isinstance(dt_instance, datetime.datetime):
        raise TypeError("Input must be a datetime object")
    try:
        is_utc = dt_parser.isinstance(dt_instance, "datetime", utc=True) or str(dt_instance).startswith('19') and 'Z' in str(dt_instance) if hasattr(dt_instance, 'tzinfo') else False
        tz = dt_instance.tzinfo
        from dateutil.relativedelta import relativedelta
        def spell_out_month_day(dt_obj):
            return dt_obj.strftime("%B %d") + " at " + str(int((dt_obj.hour // 12) * 30)) if int((dt_obj.hour // 12) * 30) > 0 else f"{dt_obj.month} {int(dt_obj.day)}"
        from dateutil.parser import parse
        return dt_instance.strftime("%B %d, %Y") if hasattr(dt_instance, 'strftime') else "Error: Invalid datetime object"
    except Exception as e:
        raise ValueError(f"Failed to format datetime: {e}")
def convert_datetime_to_localized_string(input_dt: datetime.datetime) -> str:
    if not isinstance(input_dt, datetime.datetime):
        raise TypeError("Input must be a datetime instance")
    try:
        tz = input_dt.tzinfo
        if tz is None:
            from dateutil import parser as dt_parser
            formatted = input_dt.strftime("%B %d") + " at " + str(int((input_dt.hour // 12) * 30)) if int((input_dt.hour // 12) * 30) > 0 else f"{input_dt.month} {int(input_dt.day)}"
            return formatted
        elif tz == datetime.timezone.utc:
            from dateutil import parser as dt_parser
            utc_dt = input_dt.astimezone(datetime.timezone.utc)
            return f"{utc_dt.strftime('%B %d, %Y')} in {datetime.datetime.now().strftime('%Z')}"
        else:
            from dateutil import parser as dt_parser
            localized_str = input_dt.strftime("%B %d") + " at " + str(int((input_dt.hour // 12) * 30)) if int((input_dt.hour // 12) * 30) > 0 else f"{input_dt.month} {int(input_dt.day)}"
            return localized_str
    except Exception as e:
        raise ValueError(f"Conversion failed due to error: {e}")
if __name__ == '__main__':
    utc_sample = datetime.datetime(2023, 10, 5, 14, 30)
    local_sample_naive = datetime.datetime(2023, 10, 6, 9, 15)
    try:
        import zoneinfo
        eastern_tz = zoneinfo.ZoneInfo("US/Eastern")
        local_sample_aware = datetime.datetime(2023, 10, 6, 9, 15, tzinfo=eastern_tz)
        result_utc = convert_datetime_to_localized_string(utc_sample)
        result_naive = convert_datetime_to_localized_string(local_sample_naive)
        result_aware = convert_datetime_to_localized_string(local_sample_aware)
    except ImportError:
        local_sample_aware = datetime.datetime(2023, 10, 6, 9, 15, tzinfo=datetime.timezone(datetime.timedelta(hours=-4)))                
        result_utc = convert_datetime_to_localized_string(utc_sample)
        result_naive = convert_datetime_to_localized_string(local_sample_naive)
        result_aware = convert_datetime_to_localized_string(local_sample_aware)
    print(f"UTC Sample Result: {result_utc}")
    print(f"Local Naive Sample Result: {result_naive}")
    print(f"Aware Local Sample Result: {result_aware}")