from datetime import datetime, timedelta

class WeekdayCalculator:
    def __init__(self, reference_date_str):
        self.reference_date = datetime.strptime(reference_date_str, '%Y-%m-%d')
        self.weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def get_next_weekday(self, target_weekday_name):
        target_index = self.weekday_names.index(target_weekday_name)
        current_index = self.reference_date.weekday()
        days_ahead = target_index - current_index
        if days_ahead <= 0:
            days_ahead += 7
        next_date = self.reference_date + timedelta(days=days_ahead)
        return next_date.strftime('%Y-%m-%d')

    def get_next_weekday_index(self, target_weekday_name):
        target_index = self.weekday_names.index(target_weekday_name)
        current_index = self.reference_date.weekday()
        days_ahead = target_index - current_index
        if days_ahead <= 0:
            days_ahead += 7
        return days_ahead

if __name__ == '__main__':
    calculator = WeekdayCalculator('2023-10-01')
    result_date = calculator.get_next_weekday('Friday')
    result_days = calculator.get_next_weekday_index('Friday')
    print(result_date)
    print(result_days)