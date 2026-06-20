import datetime

def get_current_day_of_week():
    today = datetime.date.today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[today.weekday()]

if __name__ == '__main__':
    current_day_name = get_current_day_of_week()
    print(f"The current day of the week is: {current_day_name}")