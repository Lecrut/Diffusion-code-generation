import datetime

def calculate_next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    return today + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    start_date_str = "2024-01-01"
    start_date = datetime.date(int(start_date_str.split('-')[0]), int(start_date_str.split('-')[1]), int(start_date_str.split('-')[2]))
    next_monday = calculate_next_monday()
    print(next_monday.strftime("%Y-%m-%d"))