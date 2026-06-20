from datetime import datetime

def format_datetime(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be an instance of datetime")
    
    formatted_dt = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_dt

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 0)
    print(format_datetime(sample_date))