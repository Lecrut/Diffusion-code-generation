import datetime

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    print(get_day_of_week(2024, 2, 29))