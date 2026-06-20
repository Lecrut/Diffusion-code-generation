import datetime

def is_valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def get_next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    next_monday = today + datetime.timedelta(days=days_until_monday)
    return next_monday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_next_monday())