import datetime
TARGET_DATE = (2024, 2, 29)

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A')
if __name__ == '__main__':
    result = get_day_of_week(*TARGET_DATE)
    print(result)