import datetime

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_current_day():
    today = datetime.date.today()
    day_index = today.weekday()
    return DAYS_OF_WEEK[day_index]

if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)