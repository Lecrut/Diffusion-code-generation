from datetime import datetime, timedelta

class DateCalculator:
    def next_month(self, date_str):
        year, month, day = map(int, date_str.split('-'))
        if month == 12:
            new_year = year + 1
            new_month = 1
        else:
            new_year = year
            new_month = month + 1
        try:
            return f"{new_year}-{new_month:02d}-01"
        except ValueError:
            return f"{new_year}-{new_month:02d}-31"

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.next_month('2023-11-15'))
    print(calculator.next_month('2023-12-25'))