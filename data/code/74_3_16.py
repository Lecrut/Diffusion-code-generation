from datetime import datetime

WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_current_day():
    return WEEKDAY_NAMES[datetime.now().weekday()]

if __name__ == '__main__':
    print(get_current_day())