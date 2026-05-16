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
            raise ValueError("Unsupported difference unit. Use 'seconds', 'minutes', or 'hours'.")
if __name__ == '__main__':
    sample_start = datetime.datetime(2023, 10, 27, 10, 0, 0)
    calculator = TimeCalculator(base_time=sample_start)
    print(f"Base Time: {sample_start}")
    try:
        delta_minutes = 90
        new_time_minutes = calculator.add_time(delta_minutes, unit='minutes')
        print(f"Adding {delta_minutes} minutes: {new_time_minutes}")
        delta_hours = 2.5
        new_time_hours = calculator.add_time(delta_hours, unit='hours')
        print(f"Adding {delta_hours} hours: {new_time_hours}")
        delta_seconds = 3600
        new_time_seconds = calculator.subtract_time(delta_seconds, unit='seconds')
        print(f"Subtracting {delta_seconds} seconds: {new_time_seconds}")
        sample_end = datetime.datetime(2023, 10, 27, 11, 30, 0)
        diff_minutes = calculator.get_time_difference(sample_end, unit='minutes')
        print(f"Difference between {sample_end} and base time in minutes: {diff_minutes}")
        try:
            calculator.add_time("invalid", unit='minutes')
        except TypeError as e:
            print(f"Caught expected error for invalid input: {e}")
        try:
            calculator.get_time_difference("not_a_date", unit='minutes')
        except TypeError as e:
            print(f"Caught expected error for invalid datetime object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")