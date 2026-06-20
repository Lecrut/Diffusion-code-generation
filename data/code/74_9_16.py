import datetime

def get_current_day_of_week():
    today = datetime.date.today()
    if not isinstance(today, datetime.date):
        return "Error determining day of the week"
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = today.weekday()
    if not (0 <= day_index < len(days)):
        return "Error determining day of the week"
    return days[day_index]

if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)