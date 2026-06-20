import datetime

class DateDifferenceCalculator:
    DAYS_PER_WEEK = 7

    @staticmethod
    def calculate_week_difference(date_str1, date_str2):
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        time_difference = abs(date2 - date1)
        weeks = time_difference.days / DateDifferenceCalculator.DAYS_PER_WEEK
        return weeks

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_week_difference("2023-01-01", "2023-01-08")
    print(result)