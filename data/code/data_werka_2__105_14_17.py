import datetime

def calculate_next_monday():
    today = datetime.date.today()
    days_until_monday = 7 - today.weekday()
    next_monday = today + datetime.timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    print(calculate_next_monday())