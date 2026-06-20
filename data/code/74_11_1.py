import datetime

class DayOfWeekFinder:
    def get_current_day_of_week(self):
        return datetime.datetime.now().strftime("%A")

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())