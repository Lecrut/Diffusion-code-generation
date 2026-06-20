from datetime import datetime

def format_datetime(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    return dt.strftime("%d/%m/%Y %I:%M %p")

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 26, 15, 45)
    print(format_datetime(sample_dt))