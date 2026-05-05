import datetime
class DayOfWeekFinder:
    def get_current_day(self):
        today = datetime.date.today()
        return today.weekday()
if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_index = finder.get_current_day()
    print(f"The current day of the week index (Monday is 0, Sunday is 6): {day_index}")