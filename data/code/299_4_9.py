from datetime import datetime

def is_weekend():
    today = datetime.now()
    return today.weekday() >= 5

if __name__ == '__main__':
    print(is_weekend())