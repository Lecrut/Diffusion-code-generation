import datetime

def get_current_day_name():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime.date.today().weekday()]

if __name__ == '__main__':
    print(f"The current day of the week is: {get_current_day_name()}")