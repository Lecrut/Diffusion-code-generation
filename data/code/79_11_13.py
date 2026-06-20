import datetime

class DateCalculator:

    def get_next_month_date(self, dt):
        if dt.month == 12:
            next_month = 1
            next_year = dt.year + 1
        else:
            next_month = dt.month + 1
            next_year = dt.year
        return datetime.date(next_year, next_month, 1)
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date_1 = datetime.datetime(2023, 10, 15)
    result_1 = calculator.get_next_month_date(sample_date_1)
    print(f'Next month after {sample_date_1.date()}: {result_1}')
    sample_date_2 = datetime.datetime(2024, 2, 29)
    result_2 = calculator.get_next_month_date(sample_date_2)
    print(f'Next month after {sample_date_2.date()}: {result_2}')