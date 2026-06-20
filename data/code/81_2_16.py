from datetime import datetime

class TimeCalculator:
    def validate_timestamp(self, timestamp_str):
        try:
            datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False

    def calculate_elapsed_hours(self, start_time_str, end_time_str):
        if not self.validate_timestamp(start_time_str) or not self.validate_timestamp(end_time_str):
            raise ValueError("Invalid timestamp format. Please use YYYY-MM-DD HH:MM:SS.")
        
        time_format = "%Y-%m-%d %H:%M:%S"
        start_time = datetime.strptime(start_time_str, time_format)
        end_time = datetime.strptime(end_time_str, time_format)
        time_difference = end_time - start_time
        elapsed_hours = time_difference.total_seconds() / 3600
        return elapsed_hours

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = "2023-01-01 10:00:00"
    end = "2023-01-03 14:30:00"
    elapsed = calculator.calculate_elapsed_hours(start, end)
    print(elapsed)