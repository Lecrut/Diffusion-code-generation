from datetime import datetime

class TimeCalculator:
    def calculate_elapsed_hours(self, start_time_str, end_time_str):
        time_format = "%Y-%m-%d %H:%M:%S"
        start_time = datetime.strptime(start_time_str, time_format)
        end_time = datetime.strptime(end_time_str, time_format)
        return self._calculate_duration_in_hours(start_time, end_time)

    @staticmethod
    def _calculate_duration_in_hours(start_time, end_time):
        time_difference = end_time - start_time
        return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = "2023-01-01 10:00:00"
    end = "2023-01-03 14:30:00"
    elapsed = calculator.calculate_elapsed_hours(start, end)
    print(elapsed)