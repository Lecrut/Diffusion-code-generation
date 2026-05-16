import datetime
class TimeCalculator:
    def __init__(self, base_time=None):
        self.base_time = base_time if base_time is not None else datetime.datetime.now()
    def add_time(self, delta, unit='seconds'):
        if unit == 'seconds':
            if isinstance(delta, (int, float)):
                new_time = self.base_time + datetime.timedelta(seconds=delta)
                return new_time
            else:
                raise TypeError("Delta for seconds must be a number.")
        elif unit == 'minutes':
            if isinstance(delta, (int, float)):
                new_time = self.base_time + datetime.timedelta(minutes=delta)
                return new_time
            else:
                raise TypeError("Delta for minutes must be a number.")
        elif unit == 'hours':
            if isinstance(delta, (int, float)):
                new_time = self.base_time + datetime.timedelta(hours=delta)
                return new_time
            else:
                raise TypeError("Delta for hours must be a number.")
        else:
            raise ValueError("Unsupported time unit. Use 'seconds', 'minutes', or 'hours'.")
    def subtract_time(self, delta, unit='seconds'):
        if unit == 'seconds':
            if isinstance(delta, (int, float)):
                new_time = self.base_time - datetime.timedelta(seconds=delta)
                return new_time
            else:
                raise TypeError("Delta for seconds must be a number.")
        elif unit == 'minutes':
            if isinstance(delta, (int, float)):
                new_time = self.base_time - datetime.timedelta(minutes=delta)
                return new_time
            else:
                raise TypeError("Delta for minutes must be a number.")
        elif unit == 'hours':
            if isinstance(delta, (int, float)):
                new_time = self.base_time - datetime.timedelta(hours=delta)
                return new_time
            else:
                raise TypeError("Delta for hours must be a number.")
        else:
            raise ValueError("Unsupported time unit. Use 'seconds', 'minutes', or 'hours'.")
    def get_time_difference(self, end_time, unit='seconds'):
        if not isinstance(end_time, datetime.datetime):
            raise TypeError("end_time must be a datetime object.")
        difference = end_time - self.base_time
        if unit == 'seconds':
            return difference.total_seconds()
        elif unit == 'minutes':
            return difference.total_seconds() / 60
        elif unit == 'hours':
            return difference.total_seconds() / 3600
        else:
            raise ValueError("Unsupported unit for difference calculation. Use 'seconds', 'minutes', or 'hours'.")
if __name__ == '__main__':
    print("--- Time Calculation Module Test ---")
    sample_start = datetime.datetime(2023, 10, 27, 10, 0, 0)
    print(f"Base Time Set To: {sample_start}")
    calculator = TimeCalculator(base_time=sample_start)
    delta_minutes = 90
    try:
        new_time_minutes = calculator.add_time(delta_minutes, unit='minutes')
        print(f"\nAdding {delta_minutes} minutes to base time:")
        print(f"Resulting Time: {new_time_minutes}")
    except (TypeError, ValueError) as e:
        print(f"Error during addition: {e}")
    delta_hours = 2.5
    try:
        new_time_hours = calculator.add_time(delta_hours, unit='hours')
        print(f"\nAdding {delta_hours} hours to base time:")
        print(f"Resulting Time: {new_time_hours}")
    except (TypeError, ValueError) as e:
        print(f"Error during addition: {e}")
    delta_seconds = 3600          
    try:
        new_time_sub = calculator.subtract_time(delta_seconds, unit='seconds')
        print(f"\nSubtracting {delta_seconds} seconds from base time:")
        print(f"Resulting Time: {new_time_sub}")
    except (TypeError, ValueError) as e:
        print(f"Error during subtraction: {e}")
    sample_end = datetime.datetime(2023, 10, 27, 11, 30, 0)
    try:
        diff_seconds = calculator.get_time_difference(sample_end, unit='seconds')
        print(f"\nTime difference between {sample_start} and {sample_end} (in seconds): {diff_seconds}")
        diff_hours = calculator.get_time_difference(sample_end, unit='hours')
        print(f"Time difference between {sample_start} and {sample_end} (in hours): {diff_hours}")
    except (TypeError, ValueError) as e:
        print(f"Error during difference calculation: {e}")
    print("\n--- Testing Error Handling ---")
    try:
        calculator.add_time("invalid", unit='minutes')
    except TypeError as e:
        print(f"Caught expected error for invalid type: {e}")
    try:
        calculator.add_time(10, unit='days')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        calculator.get_time_difference("not a date", unit='seconds')
    except TypeError as e:
        print(f"Caught expected error for invalid end_time type: {e}")