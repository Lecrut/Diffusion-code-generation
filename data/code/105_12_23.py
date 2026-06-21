from datetime import datetime, timedelta

class NextWeekdayCalculator:
    WEEKDAY_NAMES = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    @staticmethod
    def get_days_until_target(start_date, target_weekday_index):
        current_index = start_date.weekday()
        difference = target_weekday_index - current_index
        if difference <= 0:
            difference += 7
        return difference

    def compute_next_occurrence(self, start_date_str, target_weekday_index):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        days_to_add = self.get_days_until_target(start_date, target_weekday_index)
        next_date = start_date + timedelta(days=days_to_add)
        return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = NextWeekdayCalculator()
    start_date = '2023-10-01'
    target_weekday = 4
    result = calculator.compute_next_occurrence(start_date, target_weekday)
    print(result)