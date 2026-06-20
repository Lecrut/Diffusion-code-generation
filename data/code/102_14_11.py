import calendar

def is_weekday(date):
    return date.isoweekday() < 6
if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    print(is_weekday(sample_date))