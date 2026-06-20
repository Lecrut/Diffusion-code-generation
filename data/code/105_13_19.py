import datetime
WEEKEND_DAYS = (5, 6)

def find_next_weekend():
    today = datetime.date.today()
    current_day_of_week = today.weekday()
    if current_day_of_week in WEEKEND_DAYS:
        return today + datetime.timedelta(days=2)
    days_until_weekend = (5 - current_day_of_week) % 7
    next_weekend_date = today + datetime.timedelta(days=days_until_weekend)
    return next_weekend_date
if __name__ == '__main__':
    result = find_next_weekend()
    print(f'Next Weekend Date: {result}')