import datetime

def get_current_day_of_week():
    today = datetime.datetime.now()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[today.weekday()]

if __name__ == '__main__':
    print(get_current_day_of_week())