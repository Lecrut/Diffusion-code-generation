import datetime

def get_day_name(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_name(2023, 10, 25)
    print(result)