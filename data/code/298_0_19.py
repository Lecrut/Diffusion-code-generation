class TimeDifferenceCalculator:
    TIME_FORMAT = '%H:%M'

    @staticmethod
    def calculate_time_difference(time_str1: str, time_str2: str) -> int:
        time1 = datetime.datetime.strptime(time_str1, TimeDifferenceCalculator.TIME_FORMAT)
        time2 = datetime.datetime.strptime(time_str2, TimeDifferenceCalculator.TIME_FORMAT)
        diff = abs((time2 - time1).seconds)
        return diff // 60

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    t1 = "09:30"
    t2 = "14:45"
    result = calculator.calculate_time_difference(t1, t2)
    print(result)