import datetime

def get_current_day():
    today = datetime.date.today()
    day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return day_of_week[today.weekday()]

if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)