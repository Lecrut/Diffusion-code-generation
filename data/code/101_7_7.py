import datetime

class WeekdayCalculator:
    def __init__(self, date_str):
        self.date_obj = datetime.date.fromisoformat(date_str)

    def get_weekday_index(self):
        return self.date_obj.weekday()

    def get_weekday_name(self):
        names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return names[self.date_obj.weekday()]

if __name__ == '__main__':
    calc = WeekdayCalculator('2024-07-04')
    print(calc.get_weekday_index())
    print(calc.get_weekday_name())