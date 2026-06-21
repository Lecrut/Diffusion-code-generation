from datetime import date, timedelta

def find_next_weekend_date():
    today = date.today()
    days_ahead = 0
    while today.weekday() < 5:
        today += timedelta(days=1)
        days_ahead += 1
    return today

if __name__ == '__main__':
    result = find_next_weekend_date()
    print(result)