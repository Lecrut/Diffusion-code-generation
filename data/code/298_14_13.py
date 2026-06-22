from datetime import datetime

class TimeDifferenceCalculator:
    TIME_FORMAT = '%H:%M:%S'

    @staticmethod
    def time_diff_in_ms(time_str1: str, time_str2: str) -> int:
        try:
            dt1 = datetime.strptime(time_str1, TimeDifferenceCalculator.TIME_FORMAT)
            dt2 = datetime.strptime(time_str2, TimeDifferenceCalculator.TIME_FORMAT)
        except ValueError:
            return -1
        diff = abs(dt2 - dt1)
        total_seconds = int(diff.total_seconds())
        milliseconds = int(total_seconds * 1000)
        return milliseconds
if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    result = calculator.time_diff_in_ms('12:34:56', '12:35:07')
    print(result)