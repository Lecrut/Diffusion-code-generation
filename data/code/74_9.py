import datetime
def get_current_day_of_week():
    try:
        today = datetime.date.today()
        day_of_week = today.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day_of_week]
    except Exception:
        return "Error determining day of the week"
if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)