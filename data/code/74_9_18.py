import datetime

class DayOfWeek:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_current_day(self):
        today = datetime.date.today()
        day_of_week = today.weekday()
        return self.days[day_of_week]

if __name__ == '__main__':
    day_finder = DayOfWeek()
    current_day = day_finder.get_current_day()
    print(current_day)