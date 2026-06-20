from datetime import datetime

def format_datetime(dt):
    try:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except (AttributeError, ValueError) as e:
        raise ValueError("Invalid input. Please provide a datetime object.") from e

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_date = format_datetime(sample_dt)
    print(formatted_date)