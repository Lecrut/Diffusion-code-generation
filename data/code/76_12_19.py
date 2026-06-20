import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def calculate_difference(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
            date2 = datetime.datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
            return abs((date2 - date1).days)
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    difference = calculator.calculate_difference('2023-01-01', '2023-01-31')
    print(f"The difference between the two dates is {difference} days.")