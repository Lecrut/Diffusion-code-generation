import datetime

class TimeDifferenceCalculator:
    def __init__(self, time_str1, time_str2):
        self.time1 = self.parse_time(time_str1)
        self.time2 = self.parse_time(time_str2)

    @staticmethod
    def parse_time(time_str):
        return datetime.datetime.strptime(time_str, '%H:%M:%S')

    def calculate_difference(self):
        diff = abs(self.time1 - self.time2)
        return diff.total_seconds() / 3600.0

if __name__ == '__main__':
    calculator1 = TimeDifferenceCalculator("01:00:00", "05:30:00")
    print(f"Difference between 01:00:00 and 05:30:00: {calculator1.calculate_difference()} hours")

    calculator2 = TimeDifferenceCalculator("10:15:30", "10:15:30")
    print(f"Difference between 10:15:30 and 10:15:30: {calculator2.calculate_difference()} hours")