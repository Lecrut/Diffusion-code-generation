import datetime
class TimeCalculator:
    def __init__(self, base_time=None):
        self.base_time = base_time
    def add_time(self, time_delta, unit='seconds'):
        if self.base_time is None:
            raise ValueError("Base time must be set before performing calculations.")
        if unit == 'seconds':
            result = self.base_time + datetime.timedelta(seconds=time_delta)
        elif unit == 'minutes':
            result = self.base_time + datetime.timedelta(minutes=time_delta)
        elif unit == 'hours':
            result = self.base_time + datetime.timedelta(hours=time_delta)
        else:
            raise ValueError(f"Unsupported time unit: {unit}")
        return result
    def subtract_time(self, time_delta, unit='seconds'):
        if self.base_time is None:
            raise ValueError("Base time must be set before performing calculations.")
        if unit == 'seconds':
            result = self.base_time - datetime.timedelta(seconds=time_delta)
        elif unit == 'minutes':
            result = self.base_time - datetime.timedelta(minutes=time_delta)
        elif unit == 'hours':
            result = self.base_time - datetime.timedelta(hours=time_delta)
        else:
            raise ValueError(f"Unsupported time unit: {unit}")
        return result
    def get_time_difference(self, end_time, start_time):
        if start_time is None or end_time is None:
            raise ValueError("Both start_time and end_time must be provided for difference calculation.")
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise TypeError("Inputs must be datetime objects.")
        if start_time > end_time:
            raise ValueError("Start time cannot be after end time.")
        difference = end_time - start_time
        return difference
if __name__ == '__main__':
    sample_start = datetime.datetime(2023, 10, 27, 10, 0, 0)
    calculator = TimeCalculator(base_time=sample_start)
    print(f"Base Time: {sample_start}")
    try:
        delta_minutes = 90
        new_time_add = calculator.add_time(delta_minutes, unit='minutes')
        print(f"Adding {delta_minutes} minutes: {new_time_add}")
        delta_hours = 3
        new_time_add_hours = calculator.add_time(delta_hours, unit='hours')
        print(f"Adding {delta_hours} hours: {new_time_add_hours}")
        delta_seconds = 3600          
        new_time_sub = calculator.subtract_time(delta_seconds, unit='seconds')
        print(f"Subtracting {delta_seconds} seconds: {new_time_sub}")
        sample_end = datetime.datetime(2023, 10, 27, 11, 30, 0)
        diff = calculator.get_time_difference(sample_start, sample_end)
        print(f"Time difference between {sample_start} and {sample_end}: {diff}")
        try:
            calculator.add_time(10, unit='days')
        except ValueError as e:
            print(f"Caught expected error for invalid unit: {e}")
        try:
            calculator.subtract_time(10, unit='minutes')
        except ValueError as e:
            print(f"Caught expected error for missing base time: {e}")
        try:
            calculator.get_time_difference(sample_end, sample_start)
        except ValueError as e:
            print(f"Caught expected error for start > end: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")