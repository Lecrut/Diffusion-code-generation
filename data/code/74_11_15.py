import datetime

class DayOfWeekFinder:
    def get_current_day_of_week(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_weekday_index = datetime.datetime.now().weekday()
        return days[current_weekday_index]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())