from datetime import date, timedelta

class DateCalculator:
    def calculate_next_friday(self, reference_date: date) -> str:
        days_until_friday = (4 - reference_date.weekday()) % 7
        if days_until_friday == 0:
            days_until_friday = 7
        return (reference_date + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = date(2023, 12, 15)
    next_friday_str = calculator.calculate_next_friday(sample_date)
    print(next_friday_str)