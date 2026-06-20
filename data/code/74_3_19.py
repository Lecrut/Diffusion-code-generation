from datetime import datetime

DAY_NAMES = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

if __name__ == '__main__':
    today = datetime.now()
    day_index = today.weekday()
    print(DAY_NAMES[day_index])