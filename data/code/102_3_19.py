import datetime

def is_weekday(date):
    return date.weekday() < 5

if __name__ == '__main__':
    current_date = datetime.date(2023, 10, 26)
    result = is_weekday(current_date)
    print(result)