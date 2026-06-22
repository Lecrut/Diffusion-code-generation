import datetime
import calendar

def is_weekday(date_str: str) -> bool:
    parts = date_str.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    date_obj = datetime.date(year, month, day)
    is_weekday_check = date_obj.weekday() < 5
    return is_weekday_check

if __name__ == '__main__':
    test_date = "2024-02-03"
    result = is_weekday(test_date)
    print(result)