from datetime import datetime

class TimeCalculator:
    def calculate_elapsed_hours(self, start_time_str, end_time_str):
        time_format = "%Y-%m-%d %H:%M:%S"
        start_time = datetime.strptime(start_time_str, time_format)
        end_time = datetime.strptime(end_time_str, time_format)
        return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = "2023-01-01 10:00:00"
    end = "2023-01-03 14:30:00"
    print(calculator.calculate_elapsed_hours(start, end))