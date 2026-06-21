import datetime

WEEKDAY_FORMAT_CODE = '%A'

def get_weekday_upper(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime(WEEKDAY_FORMAT_CODE).upper()

if __name__ == '__main__':
    year = 2024
    month = 7
    day = 4
    result = get_weekday_upper(year, month, day)
    print(result)