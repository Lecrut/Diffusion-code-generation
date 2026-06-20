def is_weekday(date):
    return date.weekday() < 5
if __name__ == '__main__':
    print(is_weekday(datetime.date(2023, 4, 10)))
    print(is_weekday(datetime.date(2023, 4, 11)))