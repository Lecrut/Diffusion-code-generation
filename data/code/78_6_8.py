import calendar

class DateCalculator:
    @staticmethod
    def date_to_month_number(date_str):
        year, month, _ = map(int, date_str.split('-'))
        return year * 12 + month
    
    @staticmethod
    def months_between_dates(date_str1, date_str2):
        return abs(DateCalculator.date_to_month_number(date_str1) - DateCalculator.date_to_month_number(date_str2))

if __name__ == '__main__':
    calculator = DateCalculator()
    result1 = calculator.months_between_dates('2020-01-01', '2023-04-15')
    print(result1)