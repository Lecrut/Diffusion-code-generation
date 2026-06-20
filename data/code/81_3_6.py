class TimeDifferenceCalculator:
    TIME_FORMAT = "%H:%M:%S"

    @staticmethod
    def parse_time(time_str):
        return datetime.datetime.strptime(time_str, TimeDifferenceCalculator.TIME_FORMAT)

    @staticmethod
    def calculate_elapsed_time(start_time_str, end_time_str):
        start_time = TimeDifferenceCalculator.parse_time(start_time_str)
        end_time = TimeDifferenceCalculator.parse_time(end_time_str)
        if end_time < start_time:
            end_time += datetime.timedelta(days=1)
        elapsed_time = end_time - start_time
        total_seconds = elapsed_time.total_seconds()
        total_hours = total_seconds / 3600.0
        return total_hours

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    elapsed = calculator.calculate_elapsed_time('09:00:00', '17:30:00')
    print(f"{elapsed}")