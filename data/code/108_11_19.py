import datetime

def get_day_of_month(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a date object")
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    return day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 3, 15)
    result = get_day_of_month(sample_date)
    print(result)