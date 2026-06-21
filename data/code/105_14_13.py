import datetime

class DateCalculator:
    def __init__(self, reference_date=None):
        if reference_date is None:
            self.reference_date = datetime.date.today()
        else:
            self.reference_date = reference_date

    def get_next_monday(self):
        current_weekday = self.reference_date.weekday()
        days_until_monday = (7 - current_weekday) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        next_monday = self.reference_date + datetime.timedelta(days=days_until_monday)
        return next_monday

    def get_next_weekday(self, target_weekday):
        current_weekday = self.reference_date.weekday()
        days_until_target = (target_weekday - current_weekday) % 7
        if days_until_target == 0:
            days_until_target = 7
        next_target = self.reference_date + datetime.timedelta(days=days_until_target)
        return next_target

if __name__ == '__main__':
    calculator = DateCalculator(datetime.date(2023, 10, 23))
    next_monday = calculator.get_next_monday()
    next_tuesday = calculator.get_next_weekday(1)
    print(next_monday)
    print(next_tuesday)