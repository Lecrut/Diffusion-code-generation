import datetime
def get_current_day():
    today = datetime.date.today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = today.weekday()
    return days[index]
if __name__ == '__main__':
    day = get_current_day()
    print(day)