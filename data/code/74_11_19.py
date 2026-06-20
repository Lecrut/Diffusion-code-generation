import datetime

class DayOfWeekFinder:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_current_day_of_week(self):
        return self.days_of_week[datetime.datetime.now().weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())