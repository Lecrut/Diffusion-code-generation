import datetime

def get_weekday(year, month, day):
    date_object = datetime.date(year, month, day)
    return date_object.weekday()

if __name__ == '__main__':
    sample_date = (2024, 7, 4)
    weekday_index = get_weekday(*sample_date)
    print(weekday_index)