import datetime

def next_multiple_of_seven(start_date):
    days_until_next_multiple = (6 - start_date.weekday()) % 7 + 1
    return start_date + datetime.timedelta(days=days_until_next_multiple)

if __name__ == '__main__':
    start_date = datetime.date(2024, 1, 1)
    next_seven_day = next_multiple_of_seven(start_date)
    print(next_seven_day)