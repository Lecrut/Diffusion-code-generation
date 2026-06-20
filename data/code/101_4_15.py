import datetime

def day_of_week(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (datetime.datetime(year, month, day).weekday() + 1) % 7

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(day_of_week(sample_date))