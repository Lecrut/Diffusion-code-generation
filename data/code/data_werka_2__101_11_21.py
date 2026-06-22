import datetime

def get_day_of_week(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)