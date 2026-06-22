import datetime

def is_weekend():
    today = datetime.datetime.today()
    return today.weekday() >= 5

if __name__ == '__main__':
    print(is_weekend())