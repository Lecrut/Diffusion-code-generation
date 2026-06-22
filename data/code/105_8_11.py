from datetime import date, timedelta

class DateCalculator:
    def __init__(self, start_date):
        self.start_date = start_date
        self.weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def days_until_weekday(self, target_weekday):
        current_weekday = self.start_date.weekday()
        difference = target_weekday - current_weekday
        if difference <= 0:
            difference += 7
        return difference

    def get_next_date(self, target_weekday):
        delta = timedelta(days=self.days_until_weekday(target_weekday))
        return self.start_date + delta

    def get_name_of_weekday(self, weekday_index):
        return self.weekday_names[weekday_index]

if __name__ == '__main__':
    start = date(2023, 9, 15)
    target = 3
    calc = DateCalculator(start)
    next_date = calc.get_next_date(target)
    name = calc.get_name_of_weekday(target)
    days = calc.days_until_weekday(target)
    print(f"{name} ({next_date}) in {days} days")
    print(next_date.isoformat())
    print(name)
    print(days)