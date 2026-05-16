import datetime
class DayOfWeekFinder:
    def get_current_day(self):
        today = datetime.date.today()
        return today.weekday()
if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_current_day()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_name = days[day_index]
    print(f"The current day of the week is: {current_day_name}")