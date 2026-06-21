import datetime

def get_day_of_month(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date instance")
    return date_obj.day

if __name__ == '__main__':
    sample_date = datetime.date(2024, 2, 29)
    result = get_day_of_month(sample_date)
    print(result)