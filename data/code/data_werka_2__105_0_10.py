from datetime import datetime, timedelta

class NextWeekdayCalculator:
    def __init__(self, start_date=None):
        if start_date is None:
            self.start_date = datetime.today()
        else:
            self.start_date = start_date
        self.target_weekday = 0

    def get_days_until_target(self):
        current_weekday = self.start_date.weekday()
        delta = (self.target_weekday - current_weekday) % 7
        if delta == 0:
            delta = 7
        return delta

    def calculate_next_occurrence(self):
        days_to_add = self.get_days_until_target()
        return self.start_date + timedelta(days=days_to_add)

    def get_formatted_date(self):
        result_date = self.calculate_next_occurrence()
        return result_date.strftime('%A, %Y-%m-%d')

if __name__ == '__main__':
    calculator = NextWeekdayCalculator()
    result_date = calculator.calculate_next_occurrence()
    formatted_result = calculator.get_formatted_date()
    print(formatted_result)
    print(f"Days until target: {calculator.get_days_until_target()}")