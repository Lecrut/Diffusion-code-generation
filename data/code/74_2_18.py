import datetime

class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        return today.weekday()

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = days[day_index]
    print(f"The current day of the week is: {current_day}")