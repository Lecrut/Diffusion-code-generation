import datetime

def is_weekend(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 7)
    result = is_weekend(sample_date)
    print(f"Is {sample_date} a weekend? {result}")