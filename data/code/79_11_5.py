from datetime import datetime, timedelta

class DateCalculator:
    def get_next_month_date(self, date_str):
        date_format = "%Y-%m-%d"
        current_date = datetime.strptime(date_str, date_format)
        next_month_date = current_date.replace(day=1) + timedelta(days=32)
        return next_month_date.strftime(date_format)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = "2023-04-15"
    print(calculator.get_next_month_date(sample_date))