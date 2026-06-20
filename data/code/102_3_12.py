import datetime

def is_weekday():
    today = datetime.date.today()
    return today.weekday() < 5

if __name__ == '__main__':
    print(is_weekday())