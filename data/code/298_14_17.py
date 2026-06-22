class TimeDifferenceCalculator:
    def __init__(self):
        self.time_format = "%H:%M:%S"

    def calculate_time_difference(self, time_str1: str, time_str2: str) -> int:
        time1 = datetime.strptime(time_str1, self.time_format)
        time2 = datetime.strptime(time_str2, self.time_format)
        diff = abs(time2 - time1)
        total_seconds = diff.total_seconds()
        return int(total_seconds * 1000)

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    result = calculator.calculate_time_difference("14:30:00", "16:45:30")
    print(result)