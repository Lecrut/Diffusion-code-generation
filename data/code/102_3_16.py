import datetime

def is_weekday():
    return datetime.datetime.now().weekday() < 5

if __name__ == '__main__':
    print(is_weekday())