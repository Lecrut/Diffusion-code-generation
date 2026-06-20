import datetime

def get_next_monday():
    today = datetime.datetime.now()
    days_to_add = (7 - today.weekday() + 1) % 7
    next_monday = today + datetime.timedelta(days=days_to_add)
    return next_monday.date()

if __name__ == '__main__':
    print(get_next_monday())