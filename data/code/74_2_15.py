import datetime

class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        return today.strftime("%A")

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    day_name = finder.get_today()
    print(f"The current day is: {day_name}")