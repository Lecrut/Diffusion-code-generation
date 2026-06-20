from datetime import datetime, timedelta

class DateCalculator:
    def next_month(self, date_str):
        date_format = "%Y-%m-%d"
        date_obj = datetime.strptime(date_str, date_format)
        next_month = (date_obj.replace(day=28) + timedelta(days=4)).replace(day=1)
        return next_month.strftime(date_format)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.next_month("2023-09-15"))