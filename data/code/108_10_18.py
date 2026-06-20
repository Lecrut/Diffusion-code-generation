import datetime

def get_day_of_week(year, month, day):
    return datetime.date(year, month, day).strftime('%A')

if __name__ == '__main__':
    print(get_day_of_week(2024, 1, 1))