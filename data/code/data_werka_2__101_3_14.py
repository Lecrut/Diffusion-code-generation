from datetime import date

class WeekdayFinder:
    def __init__(self, target_date):
        self.target_date = target_date

    def get_name(self):
        return self.target_date.strftime("%A")

    def get_number(self):
        return self.target_date.weekday()

if __name__ == '__main__':
    finder = WeekdayFinder(date(2023, 12, 25))
    print(finder.get_name())
    print(finder.get_number())