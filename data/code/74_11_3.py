import datetime

class DayOfWeekFinder:
    def get_current_day_of_week(self):
        try:
            now = datetime.datetime.now()
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return days[now.weekday()]
        except Exception as e:
            raise ValueError("Failed to determine the current day of the week") from e

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())