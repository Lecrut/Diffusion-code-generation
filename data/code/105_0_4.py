import datetime

def next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    return today + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    try:
        next_monday_date = next_monday()
        print(next_monday_date.strftime("%Y-%m-%d"))
    except Exception as e:
        print(f"An error occurred: {e}")