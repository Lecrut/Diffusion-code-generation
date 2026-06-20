from datetime import date

class DateDifferenceCalculator:
    START_DATE = '2023-01-01'
    END_DATE = '2023-01-31'

    @staticmethod
    def calculate_days(start_date_str, end_date_str):
        start_date = date.fromisoformat(start_date_str)
        end_date = date.fromisoformat(end_date_str)
        return (end_date - start_date).days

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    days = calculator.calculate_days(DateDifferenceCalculator.START_DATE, DateDifferenceCalculator.END_DATE)
    print(days)