import datetime

def get_day_of_month(date_obj):
    if not hasattr(date_obj, 'day'):
        raise ValueError("Input must have a 'day' attribute")
    return date_obj.day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 3, 15)
    day_value = get_day_of_month(sample_date)
    print(day_value)