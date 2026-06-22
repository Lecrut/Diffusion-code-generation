from datetime import date, timedelta

class DateCalculator:
    def __init__(self, reference):
        self.reference = reference
        self.days_offset = None

    def calculate_days_until_friday(self):
        current_weekday = self.reference.weekday()
        target_weekday = 4
        diff = target_weekday - current_weekday
        if diff <= 0:
            diff += 7
        self.days_offset = diff
        return diff

    def get_friday(self):
        if self.days_offset is None:
            self.calculate_days_until_friday()
        return self.reference + timedelta(days=self.days_offset)

    def get_friday_string(self):
        return self.get_friday().isoformat()

if __name__ == '__main__':
    calculator = DateCalculator(date(2023, 12, 15))
    days = calculator.calculate_days_until_friday()
    friday = calculator.get_friday()
    print(friday)
    print(calculator.get_friday_string())