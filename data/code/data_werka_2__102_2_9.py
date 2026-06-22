import datetime

def is_weekday(date_obj):
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 23)
    print(is_weekday(sample_date))