from datetime import datetime

def format_datetime_to_iso(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 11, 15, 9, 45, 30)
    formatted_date = format_datetime_to_iso(sample_dt)
    print(formatted_date)