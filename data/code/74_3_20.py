from datetime import datetime

def get_current_day():
    return datetime.now().strftime('%A')

if __name__ == '__main__':
    today = datetime.today()
    day_of_week = get_current_day(today)
    print(day_of_week)