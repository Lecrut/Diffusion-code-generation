from datetime import date

class WeekdayFinder:
    def __init__(self):
        self.weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def determine_weekday(self, year: int, month: int, day: int) -> str:
        date_obj = date(year, month, day)
        return self.weekday_names[date_obj.weekday()]

if __name__ == '__main__':
    finder = WeekdayFinder()
    print(finder.determine_weekday(2023, 10, 10))