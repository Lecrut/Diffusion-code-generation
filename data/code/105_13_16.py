import datetime

def find_next_weekend():
    today = datetime.date.today()
    days_to_add = 0
    while True:
        next_date = today + datetime.timedelta(days=days_to_add)
        if next_date.weekday() >= 5:
            return next_date
        days_to_add += 1
if __name__ == '__main__':
    result = find_next_weekend()
    print(f'Next Weekend Date: {result}')