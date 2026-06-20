import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_current_day_of_week():
        current_day_index = datetime.datetime.now().weekday()
        return DayOfWeekFinder.DAYS_OF_WEEK[current_day_index]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(finder.get_current_day_of_week())