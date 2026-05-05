import datetime
def get_current_day_of_week():
    try:
        today = datetime.date.today()
        day_of_week = today.weekday()
        return day_of_week
    except Exception:
        return None
if __name__ == '__main__':
    day = get_current_day_of_week()
    if day is not None:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_name = days_of_week[day]
        print(f"The current day of the week is: {day_name}")
    else:
        print("An error occurred while determining the day of the week.")