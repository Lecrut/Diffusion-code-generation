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
if __name__ == '__main__':
    print("--- Time Calculation Module Test ---")
    start_time = datetime.datetime(2023, 10, 27, 10, 30, 0)
    print(f"Base Time: {start_time}")
    calculator = TimeCalculator(base_time=start_time)
    delta_seconds = 3600          
    try:
        time_after_seconds = calculator.add_time(delta_seconds, unit='seconds')
        print(f"Adding {delta_seconds} seconds: {time_after_seconds}")
    except (TypeError, ValueError) as e:
        print(f"Error adding seconds: {e}")
    delta_minutes = 90
    try:
        time_after_minutes = calculator.add_time(delta_minutes, unit='minutes')
        print(f"Adding {delta_minutes} minutes: {time_after_minutes}")
    except (TypeError, ValueError) as e:
        print(f"Error adding minutes: {e}")
    delta_hours = 2
    try:
        time_before_hours = calculator.subtract_time(delta_hours, unit='hours')
        print(f"Subtracting {delta_hours} hours: {time_before_hours}")
    except (TypeError, ValueError) as e:
        print(f"Error subtracting hours: {e}")
    try:
        calculator.add_time(10, unit='days')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        calculator.add_time("invalid", unit='seconds')
    except TypeError as e:
        print(f"Caught expected error for invalid delta type: {e}")