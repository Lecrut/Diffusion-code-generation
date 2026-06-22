import datetime

def is_weekend(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 7)
    print(f"Is {sample_date} a weekend? {is_weekend(sample_date)}")