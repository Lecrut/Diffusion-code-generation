class TimeDifferenceCalculator:
    TIME_FORMAT = '%H:%M'

    @staticmethod
    def parse_time(time_str: str) -> datetime:
        try:
            return datetime.strptime(time_str, TimeDifferenceCalculator.TIME_FORMAT)
        except ValueError:
            raise ValueError("Invalid time format. Expected 'HH:MM'.")

    @staticmethod
    def calculate_difference(time1: datetime, time2: datetime) -> int:
        difference = (time2 - time1).seconds // 60
        return abs(difference)

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    time_a = "01:00"
    time_b = "03:30"
    parsed_time1 = calculator.parse_time(time_a)
    parsed_time2 = calculator.parse_time(time_b)
    difference_in_minutes = calculator.calculate_difference(parsed_time1, parsed_time2)
    print(f"Time Difference (minutes): {difference_in_minutes}")