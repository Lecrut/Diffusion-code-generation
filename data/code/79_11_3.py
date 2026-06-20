from datetime import datetime, timedelta

class DateCalculator:
    def get_next_month_date(self, date_str):
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        next_month = (input_date.replace(day=28) + timedelta(days=4)).replace(day=1)
        return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = '2023-04-15'
    print(calculator.get_next_month_date(sample_date))