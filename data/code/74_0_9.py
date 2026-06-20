import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[now.weekday()]

if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)