import datetime

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2024, 2, 29)
    print(result)