import datetime
class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        return today.weekday()
if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"The index of today is: {day_index}")
    print(f"Today is: {days[day_index]}")