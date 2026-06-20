import datetime

class DateDifferenceCalculator:
    WEEKS_PER_DAY = 7

    @staticmethod
    def date_difference_in_weeks(date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        time_difference = abs((date1 - date2).days)
        difference_in_weeks = time_difference / DateDifferenceCalculator.WEEKS_PER_DAY
        return difference_in_weeks

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.date_difference_in_weeks("2023-01-01", "2023-01-29")
    print(result)