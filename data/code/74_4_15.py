from datetime import datetime

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def validate_date(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object")

def get_full_day_name(date_obj):
    validate_date(date_obj)
    return DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_full_day_name(sample_date))