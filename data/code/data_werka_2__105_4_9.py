from datetime import date, timedelta

class DateCalculator:
    SATURDAY_INDEX = 5

    @staticmethod
    def get_next_saturday(current_date):
        days_ahead = DateCalculator.SATURDAY_INDEX - current_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return current_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    fixed_date = date(2023, 11, 1)
    calculator = DateCalculator()
    result = calculator.get_next_saturday(fixed_date)
    print(result)