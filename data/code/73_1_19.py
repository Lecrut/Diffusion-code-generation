from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def calculate_time_diff(date_str1, date_str2):
        dt1 = datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
        dt2 = datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
        return dt2 - dt1

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    diff = calculator.calculate_time_diff("2023-01-01T10:00:00", "2023-01-05T14:30:00")
    print(diff)