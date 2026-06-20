from datetime import datetime

def format_datetime_with_timezone(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S%z')[:-2]

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(format_datetime_with_timezone(sample_dt))