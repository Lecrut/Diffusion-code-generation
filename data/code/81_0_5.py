from datetime import datetime

class TimeCalculator:
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def calculate_elapsed_hours(start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, TimeCalculator.TIME_FORMAT)
        end_time = datetime.strptime(end_time_str, TimeCalculator.TIME_FORMAT)
        time_difference = end_time - start_time
        elapsed_seconds = time_difference.total_seconds()
        elapsed_hours = elapsed_seconds / 3600.0
        return elapsed_hours

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.calculate_elapsed_hours("2023-10-27 09:00:00", "2023-10-27 17:30:00")
    print(result)