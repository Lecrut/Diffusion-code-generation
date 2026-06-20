class TimeCalculator:
    TIME_FORMAT = "%H:%M:%S"

    @staticmethod
    def calculate_elapsed_time(start_time_str, end_time_str):
        start_time = datetime.datetime.strptime(start_time_str, TimeCalculator.TIME_FORMAT)
        end_time = datetime.datetime.strptime(end_time_str, TimeCalculator.TIME_FORMAT)
        if end_time < start_time:
            end_time += datetime.timedelta(days=1)
        elapsed_time = end_time - start_time
        total_seconds = elapsed_time.total_seconds()
        total_hours = total_seconds / 3600.0
        return total_hours

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed = calculator.calculate_elapsed_time("09:00:00", "17:30:00")
    print(f"{elapsed}")