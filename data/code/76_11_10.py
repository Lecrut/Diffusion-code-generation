from datetime import date

class DateCalculator:
    START_DATE = '2023-01-01'
    END_DATE = '2023-01-31'

    @staticmethod
    def days_difference(start_date, end_date):
        return (date.fromisoformat(end_date) - date.fromisoformat(start_date)).days

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.days_difference(DateCalculator.START_DATE, DateCalculator.END_DATE)
    print(result)