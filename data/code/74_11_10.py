import datetime

class DayOfWeekFinder:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_current_day_of_week(self):
        return self.days[datetime.datetime.now().weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())