import datetime
def get_current_day():
    today = datetime.date.today()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = today.weekday()
    return days_of_week[day_index]
if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)