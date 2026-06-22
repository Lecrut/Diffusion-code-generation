class TimeCalculator:
    TIME_FORMAT = '%H:%M'

    @staticmethod
    def time_to_minutes(time_str: str) -> int:
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    @classmethod
    def calculate_time_difference(cls, time_str1: str, time_str2: str) -> int:
        time1_minutes = cls.time_to_minutes(time_str1)
        time2_minutes = cls.time_to_minutes(time_str2)
        return abs(time1_minutes - time2_minutes)

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = "09:30"
    t2 = "14:45"
    result = calculator.calculate_time_difference(t1, t2)
    print(result)