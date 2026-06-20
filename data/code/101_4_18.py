import datetime
WEEKDAY_OFFSET = 3

def day_of_week(date_str):
    year, month, day = map(int, date_str.split('-'))
    date_obj = datetime.date(year, month, day)
    return (date_obj.weekday() - WEEKDAY_OFFSET) % 7
if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(day_of_week(sample_date))