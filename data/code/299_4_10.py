from datetime import datetime

def is_weekend():
    return datetime.now().weekday() >= 5

if __name__ == '__main__':
    print(is_weekend())