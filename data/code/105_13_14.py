import datetime

def is_weekend(date):
    return date.weekday() >= 5

def find_next_weekend():
    today = datetime.date.today()
    days_to_add = 1
    while not is_weekend(today + datetime.timedelta(days=days_to_add)):
        days_to_add += 1
    return today + datetime.timedelta(days=days_to_add)

if __name__ == '__main__':
    next_weekend = find_next_weekend()
    print(f"Next Weekend Date: {next_weekend}")