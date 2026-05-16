from datetime import date, timedelta
class DateCalculator:
    def calculate_next_date(self, current_date):
        next_date = current_date + timedelta(days=1)
        return next_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = date(2023, 10, 26)
    next_date_str = calculator.calculate_next_date(sample_date)
    print(next_date_str)