from datetime import date, timedelta

class WeekdayCalculator:
    def __init__(self, reference_date):
        self.reference_date = reference_date

    def get_next_occurrence(self, target_weekday):
        current_weekday = self.reference_date.weekday()
        days_until_target = (target_weekday - current_weekday) % 7
        if days_until_target == 0:
            days_until_target = 7
        return self.reference_date + timedelta(days=days_until_target)

    def get_days_until(self, target_weekday):
        current_weekday = self.reference_date.weekday()
        days_until_target = (target_weekday - current_weekday) % 7
        if days_until_target == 0:
            days_until_target = 7
        return days_until_target

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_weekday = 3
    calculator = WeekdayCalculator(start_date)
    next_date = calculator.get_next_occurrence(target_weekday)
    days_count = calculator.get_days_until(target_weekday)
    print(next_date)
    print(days_count)