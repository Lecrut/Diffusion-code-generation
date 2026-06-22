from datetime import date

def is_weekend():
    today = date.today()
    return today.weekday() >= 5

if __name__ == '__main__':
    print(is_weekend())