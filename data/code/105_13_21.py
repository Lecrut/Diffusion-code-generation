from datetime import date, timedelta

def get_next_weekend_date():
    today = date.today()
    weekday = today.weekday()
    if weekday == 5:
        return today
    if weekday == 6:
        return today
    days_to_add = 5 - weekday
    return today + timedelta(days=days_to_add)

if __name__ == '__main__':
    result = get_next_weekend_date()
    print(result)