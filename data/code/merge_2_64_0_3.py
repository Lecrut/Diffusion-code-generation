import datetime
def format_full_month(date_obj: datetime.datetime) -> str:
    return date_obj.strftime("%B")
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=5)))
    result = format_full_month(sample_date)
    print(result)