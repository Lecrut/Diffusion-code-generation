from datetime import datetime

class TimeDifferenceCalculator:
    TIME_FORMAT = "%H:%M"

    @staticmethod
    def parse_time(time_str):
        return datetime.strptime(time_str, TimeDifferenceCalculator.TIME_FORMAT)

    @staticmethod
    def calculate_difference(time1, time2):
        diff = abs(time2 - time1)
        return diff.total_seconds()

if __name__ == '__main__':
    time1 = TimeDifferenceCalculator.parse_time('14:30')
    time2 = TimeDifferenceCalculator.parse_time('16:45')
    result = TimeDifferenceCalculator.calculate_difference(time1, time2)
    print(int(result))