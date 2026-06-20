import datetime

if __name__ == '__main__':
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_name = days[datetime.date.today().weekday()]
    print(f"The current day of the week is: {current_day_name}")