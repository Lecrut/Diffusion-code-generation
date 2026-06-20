from datetime import datetime

def format_datetime_to_iso8601(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(format_datetime_to_iso8601(sample_dt))