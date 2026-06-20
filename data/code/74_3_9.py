from datetime import datetime

def get_current_day():
    return datetime.now().strftime('%A')

if __name__ == '__main__':
    current_date = datetime.now()
    day_of_week = get_current_day(current_date)
    print(day_of_week)