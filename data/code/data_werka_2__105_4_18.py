from datetime import date, timedelta

WEEKDAY_MAP = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
TARGET_WEEKDAY_INDEX = 5

class DateCalculator:
    def __init__(self, start_date: date):
        if not isinstance(start_date, date):
            raise ValueError("start_date must be a date object")
        self.start_date = start_date

    def get_target_day_name(self, target_index):
        if target_index < 0 or target_index > 6:
            raise ValueError("Invalid weekday index")
        return WEEKDAY_MAP[target_index]

    def find_next_weekday(self, target_index):
        current_index = self.start_date.weekday()
        if current_index == target_index:
            return self.start_date
        days_offset = target_index - current_index
        if days_offset <= 0:
            days_offset += 7
        return self.start_date + timedelta(days=days_offset)

if __name__ == '__main__':
    fixed_start = date(2023, 11, 1)
    calculator = DateCalculator(fixed_start)
    saturday_name = calculator.get_target_day_name(TARGET_WEEKDAY_INDEX)
    result_date = calculator.find_next_weekday(TARGET_WEEKDAY_INDEX)
    print(f"{saturday_name}: {result_date}")