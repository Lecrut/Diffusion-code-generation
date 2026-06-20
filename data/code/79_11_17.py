import datetime

class DateCalculator:
    def get_next_month_date(self, date_str):
        input_date = self._validate_and_parse(date_str)
        next_month = (input_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
        return next_month.strftime('%Y-%m-%d')

    @staticmethod
    def _validate_and_parse(date_str):
        try:
            input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        return input_date

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = '2023-10-15'
    print(f"Next month after {sample_date}: {calculator.get_next_month_date(sample_date)}")