from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def date_difference(date_str1, date_str2):
        date_format = DateDifferenceCalculator.DATE_FORMAT
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.date_difference('2023-04-01', '2023-04-15')
    print(result)