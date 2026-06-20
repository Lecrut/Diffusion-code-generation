import datetime

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        return DAYS_OF_WEEK[today.weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_name = finder.get_today()
    print(f"The current day of the week is: {day_name}")