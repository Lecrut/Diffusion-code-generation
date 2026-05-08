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
            raise ValueError(f"Unsupported time unit: {unit}. Supported units are 'seconds', 'minutes', 'hours'.")
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
            raise ValueError(f"Unsupported time unit: {unit}. Supported units are 'seconds', 'minutes', 'hours'.")
        return result
    def get_time_difference(self, start_time, end_time):
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
        time_plus = calculator.add_time(3600, unit='seconds')
        print(f"Time after adding 1 hour (seconds): {time_plus}")
        time_minus = calculator.subtract_time(7200, unit='minutes')
        print(f"Time after subtracting 2 hours (minutes): {time_minus}")
        time_diff = calculator.get_time_difference(sample_start, datetime.datetime(2023, 10, 27, 11, 30, 0))
        print(f"Time difference between {sample_start} and 11:30:00: {time_diff}")
        calculator.add_time(10, unit='minutes')
        print(f"Time after adding 10 minutes: {calculator.base_time + datetime.timedelta(minutes=10)}")
        try:
            calculator.add_time(10, unit='days')
        except ValueError as e:
            print(f"Error caught successfully: {e}")
        try:
            calculator.subtract_time(10, unit='days')
        except ValueError as e:
            print(f"Error caught successfully: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")