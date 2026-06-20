import datetime

def get_current_day():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[datetime.date.today().weekday()]

if __name__ == '__main__':
    day = get_current_day()
    print(day)