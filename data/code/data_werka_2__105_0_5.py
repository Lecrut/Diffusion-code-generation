from datetime import datetime, timedelta

def calculate_next_monday():
    today = datetime.today()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return today + timedelta(days=days_until_monday)

if __name__ == '__main__':
    next_monday = calculate_next_monday()
    print(next_monday.strftime('%Y-%m-%d'))