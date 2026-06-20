import datetime

def next_monday(date):
    days_ahead = (7 - date.weekday()) % 7
    return date + datetime.timedelta(days=days_ahead)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 9, 10)
    print(next_monday(sample_date))