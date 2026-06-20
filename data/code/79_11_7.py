from datetime import datetime, timedelta

class DateCalculator:
    def next_month(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj.month == 12:
            new_date = date_obj.replace(year=date_obj.year + 1, month=1)
        else:
            new_date = date_obj.replace(month=date_obj.month + 1)
        return new_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    next_month_date = calculator.next_month('2023-12-15')
    print(next_month_date)