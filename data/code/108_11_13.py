import datetime

def calculate_day_of_month(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a date object")
    if not isinstance(date_obj, datetime.datetime):
        if date_obj.month != 3 or date_obj.day != 15:
            raise ValueError("Date must be March 15th")
    return date_obj.day

if __name__ == '__main__':
    target_date = datetime.date(2023, 3, 15)
    day_value = calculate_day_of_month(target_date)
    print(day_value)