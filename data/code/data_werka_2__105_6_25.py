from datetime import date, timedelta

class DateCalculator:
    START_DATE = date(2024, 1, 1)
    WEEK_DAYS = 7

    @staticmethod
    def _calculate_days_offset():
        return DateCalculator.WEEK_DAYS

    def find_next_multiple_of_7(self):
        offset = self._calculate_days_offset()
        target_date = self.START_DATE + timedelta(days=offset)
        return target_date

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.find_next_multiple_of_7()
    print(result)