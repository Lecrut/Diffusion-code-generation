import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_current_day_index():
        return datetime.date.today().weekday()

    def get_today(self):
        day_index = self.get_current_day_index()
        return self.DAYS_OF_WEEK[day_index]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    today = finder.get_today()
    print(f"The current day of the week is: {today}")