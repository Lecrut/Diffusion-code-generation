from datetime import datetime

def format_custom_datetime(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be an instance of datetime")
    
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 9, 15, 14, 30, 0)
    print(format_custom_datetime(sample_dt))