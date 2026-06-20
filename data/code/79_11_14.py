from datetime import datetime, timedelta

class DateCalculator:
    def next_month(self, date_str):
        date_format = "%Y-%m-%d"
        current_date = datetime.strptime(date_str, date_format)
        if current_date.month == 12:
            next_month = current_date.replace(year=current_date.year + 1, month=1)
        else:
            next_month = current_date.replace(month=current_date.month + 1)
        return next_month.strftime(date_format)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.next_month("2023-11-15"))