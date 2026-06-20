import datetime

class DateCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def calculate_days(date1_str, date2_str):
        try:
            date1 = datetime.datetime.strptime(date1_str, DateCalculator.DATE_FORMAT).date()
            date2 = datetime.datetime.strptime(date2_str, DateCalculator.DATE_FORMAT).date()
            difference = abs(date1 - date2)
            return difference.days
        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_days("2023-01-15", "2023-03-20")
    print(result)