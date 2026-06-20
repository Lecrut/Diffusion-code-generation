from datetime import datetime

class TimeDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    @staticmethod
    def calculate_time_difference(date_str1, date_str2):
        try:
            date1 = datetime.strptime(date_str1, TimeDifferenceCalculator.DATE_FORMAT)
            date2 = datetime.strptime(date_str2, TimeDifferenceCalculator.DATE_FORMAT)
            time_difference = abs(date1 - date2)
            return int(time_difference.total_seconds())
        except ValueError:
            return -1

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    result = calculator.calculate_time_difference("2023-10-27 10:00:00", "2023-10-27 10:05:30")
    print(result)