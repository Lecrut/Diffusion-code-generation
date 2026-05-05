import datetime
def get_current_day():
    today = datetime.date.today()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = today.weekday()
    return days_of_week[index]
if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)