from datetime import datetime, timedelta

def get_next_monday():
    today = datetime.now()
    days_to_monday = (7 - today.weekday()) % 7
    next_monday = today + timedelta(days=days_to_monday)
    return next_monday.date()

if __name__ == '__main__':
    print(get_next_monday())