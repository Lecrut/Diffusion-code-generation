from datetime import datetime

def validate_datetime(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Provided object is not an instance of datetime")

def format_custom_datetime(date_obj):
    validate_datetime(date_obj)
    formatted_dt = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_dt

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15, 14, 30, 0)
    print(format_custom_datetime(sample_date))