import datetime

def is_valid_date(date_obj):
    return isinstance(date_obj, datetime.date)

def get_day_of_month(date_obj):
    if not is_valid_date(date_obj):
        raise ValueError("Invalid date object")
    return date_obj.day

if __name__ == '__main__':
    date1 = datetime.date(2023, 3, 15)
    print(f"Day of month for {date1}: {get_day_of_month(date1)}")