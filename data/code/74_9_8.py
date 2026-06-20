import datetime

def get_current_day_of_week():
    today = datetime.datetime.now()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[today.weekday()]

if __name__ == '__main__':
    print(get_current_day_of_week())