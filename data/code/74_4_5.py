from datetime import datetime

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_full_day_name(date_obj):
    return DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_full_day_name(sample_date))