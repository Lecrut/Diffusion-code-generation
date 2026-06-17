import datetime as dt
def format_full_month(date_obj: dt.datetime) -> str:
    return date_obj.strftime("%B")
if __name__ == '__main__':
    sample_date = dt.datetime(2023, 10, 5, 14, 30, tzinfo=dt.timezone.utc)
    result = format_full_month(sample_date)
    print(result)