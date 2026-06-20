from datetime import datetime

def get_full_day_name(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object")
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_full_day_name(sample_date))