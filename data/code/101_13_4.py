import datetime

def get_weekday(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A').upper()

if __name__ == '__main__':
    print(get_weekday(2024, 7, 4))