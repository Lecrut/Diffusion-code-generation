import datetime

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_current_day_name():
    return DAYS_OF_WEEK[datetime.date.today().weekday()]

if __name__ == '__main__':
    print(f"The current day of the week is: {get_current_day_name()}")