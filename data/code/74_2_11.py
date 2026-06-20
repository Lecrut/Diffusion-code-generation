import datetime

class DayOfWeekFinder:
    def get_today(self):
        today = datetime.date.today()
        day_index = today.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day_index]

if __name__ == '__main__':
    finder = DayOfWeekFinder()
    print(f"The current day is: {finder.get_today()}")