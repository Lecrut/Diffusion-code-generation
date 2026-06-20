import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_today():
        today = datetime.date.today()
        return today.weekday()

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_today()
    day_name = DayOfWeekFinder.DAYS_OF_WEEK[day_index]
    print(f"The current day index (0=Monday, 6=Sunday) is: {day_index}")
    print(f"The current day is: {day_name}")