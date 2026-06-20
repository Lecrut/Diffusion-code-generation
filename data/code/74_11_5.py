import datetime

DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

class DayOfWeekFinder:
    def get_current_day_of_week(self):
        now = datetime.datetime.now()
        return DAYS_OF_WEEK[now.weekday()]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())