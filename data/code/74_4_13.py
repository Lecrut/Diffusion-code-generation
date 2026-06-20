from datetime import datetime

def get_full_day_name(date_obj):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 6)
    print(get_full_day_name(sample_date))