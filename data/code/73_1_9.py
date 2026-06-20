from datetime import datetime, timedelta

class DateDiffCalculator:
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

    @staticmethod
    def calculate_time_diff(date_str1, date_str2):
        dt1 = datetime.strptime(date_str1, DateDiffCalculator.DATE_FORMAT)
        dt2 = datetime.strptime(date_str2, DateDiffCalculator.DATE_FORMAT)
        return dt2 - dt1

if __name__ == '__main__':
    calculator = DateDiffCalculator()
    sample_date1 = "2023-10-01T12:00:00+0000"
    sample_date2 = "2023-10-01T14:30:00+0000"
    diff = calculator.calculate_time_diff(sample_date1, sample_date2)
    print(diff.total_seconds())