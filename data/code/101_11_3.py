from datetime import datetime

def get_day_of_week(year, month, day):
    date = datetime(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 10))