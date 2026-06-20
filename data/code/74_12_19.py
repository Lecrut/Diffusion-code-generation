import datetime

if __name__ == '__main__':
    today = datetime.date.today()
    day_index = today.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_name = days[day_index]
    print(f"The current day of the week is: {current_day_name}")