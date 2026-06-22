import datetime

def format_datetime(dt_obj: datetime.datetime) -> str:
    return dt_obj.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime(sample_dt)
    print(result)