import datetime
class TimeCalculator:
    def __init__(self, base_format="%Y-%m-%d %H:%M:%S"):
        self.base_format = base_format
    def parse_time(self, time_str):
        try:
            dt = datetime.datetime.strptime(time_str, self.base_format)
            return dt
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected '{self.base_format}': {e}")
    def add_duration(self, dt, duration_str):
        try:
            duration = datetime.timedelta(seconds=int(duration_str))
            new_dt = dt + duration
            return new_dt
        except ValueError:
            raise ValueError("Invalid duration format. Must be an integer number of seconds.")
    def format_time(self, dt, output_format="%Y-%m-%d %H:%M:%S"):
        try:
            return dt.strftime(output_format)
        except Exception as e:
            raise RuntimeError(f"Error formatting time: {e}")
if __name__ == '__main__':
    calculator = TimeCalculator()
    sample_date_str = "2023-10-27 10:00:00"
    sample_duration_str = "3600"
    try:
        start_time = calculator.parse_time(sample_date_str)
        print(f"Start Time: {calculator.format_time(start_time)}")
        end_time = calculator.add_duration(start_time, sample_duration_str)
        print(f"End Time (after adding {sample_duration_str} seconds): {calculator.format_time(end_time)}")
        another_time_str = "2024-01-01 00:00:00"
        another_duration_str = "86400"
        start_time_2 = calculator.parse_time(another_time_str)
        end_time_2 = calculator.add_duration(start_time_2, another_duration_str)
        print(f"Second Test: Start Time: {calculator.format_time(start_time_2)}, End Time: {calculator.format_time(end_time_2)}")
        try:
            calculator.parse_time("27/10/2023 10:00")
        except ValueError as e:
            print(f"Error Handling Test Passed: {e}")
    except ValueError as e:
        print(f"A critical error occurred during time calculation: {e}")
    except RuntimeError as e:
        print(f"A formatting error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")