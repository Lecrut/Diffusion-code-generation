import datetime

def get_day_of_week():
    today = datetime.date.today()
    weekday_index = today.weekday()
    if not (0 <= weekday_index <= 6):
        raise ValueError("Invalid weekday index")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_index]

if __name__ == '__main__':
    current_day = get_day_of_week()
    print(current_day)