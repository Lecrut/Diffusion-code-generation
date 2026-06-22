from datetime import datetime, timedelta

class MondayFinder:
    target_weekday = 0
    week_length = 7

    def __init__(self, reference_date=None):
        if reference_date is None:
            self.reference_date = datetime.today()
        else:
            self.reference_date = reference_date

    def _calculate_days_offset(self):
        current_weekday = self.reference_date.weekday()
        difference = self.target_weekday - current_weekday
        if difference <= 0:
            return self.week_length
        return difference

    def get_next_monday(self):
        days_offset = self._calculate_days_offset()
        return self.reference_date + timedelta(days=days_offset)

    def get_formatted_monday(self):
        next_monday = self.get_next_monday()
        return next_monday.strftime('%Y-%m-%d')

    def get_reference_date_str(self):
        return self.reference_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    finder = MondayFinder()
    reference_str = finder.get_reference_date_str()
    next_monday_str = finder.get_formatted_monday()
    print(f'Reference: {reference_str}')
    print(f'Next Monday: {next_monday_str}')

    specific_date = datetime(2023, 10, 5)
    specific_finder = MondayFinder(specific_date)