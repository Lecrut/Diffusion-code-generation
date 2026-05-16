import datetime
class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        return today.weekday()
if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"Today's index (0=Monday): {day_index}")
    print(f"Today's day: {days[day_index]}")