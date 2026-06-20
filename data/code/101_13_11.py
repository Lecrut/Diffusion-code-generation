import datetime

def get_weekday():
    date = datetime.date(2024, 7, 4)
    weekday = date.strftime("%A").upper()
    return weekday

if __name__ == '__main__':
    print(get_weekday())