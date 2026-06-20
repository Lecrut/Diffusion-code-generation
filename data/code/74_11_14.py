import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_current_day_of_week(self):
        return self.DAYS_OF_WEEK[datetime.datetime.now().weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())