import datetime

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_current_day():
    today = datetime.date.today()
    return DAYS_OF_WEEK[today.weekday()]

if __name__ == '__main__':
    current_day_name = get_current_day()
    print(f"The current day of the week is: {current_day_name}")