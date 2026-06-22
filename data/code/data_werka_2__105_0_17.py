from datetime import datetime, timedelta

WEEKDAY_MAP = {
    0: 7,
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
}

def calculate_next_monday():
    today = datetime.today()
    current_weekday = today.weekday()
    days_to_add = WEEKDAY_MAP.get(current_weekday, 0)
    if days_to_add == 0:
        days_to_add = 7
    return today + timedelta(days=days_to_add)

if __name__ == '__main__':
    result = calculate_next_monday()
    print(result.strftime('%Y-%m-%d'))