import datetime

def get_weekday(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    print(get_weekday(2024, 7, 4))