import datetime

class DayOfWeekFinder:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_today(self):
        today = datetime.date.today()
        return today.weekday()

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_today()
    print(f"The current day index (0=Monday, 6=Sunday) is: {day_index}")
    print(f"The current day is: {DayOfWeekFinder.DAYS_OF_WEEK[day_index]}")