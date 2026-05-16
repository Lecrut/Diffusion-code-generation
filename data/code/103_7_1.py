import datetime
class TimeCalculator:
    def __init__(self, base_time=None):
        self.base_time = base_time
    def add_time(self, delta, unit='seconds'):
        if self.base_time is None:
            raise ValueError("Base time must be set before performing calculations.")
        if unit == 'seconds':
            result = self.base_time + datetime.timedelta(seconds=delta)
        elif unit == 'minutes':
            result = self.base_time + datetime.timedelta(minutes=delta)
        elif unit == 'hours':
            result = self.base_time + datetime.timedelta(hours=delta)
        else:
            raise ValueError("Unsupported time unit. Use 'seconds', 'minutes', or 'hours'.")
        return result
    def subtract_time(self, delta, unit='seconds'):
        if self.base_time is None:
            raise ValueError("Base time must be set before performing calculations.")
        if unit == 'seconds':
            result = self.base_time - datetime.timedelta(seconds=delta)
        elif unit == 'minutes':
            result = self.base_time - datetime.timedelta(minutes=delta)
        elif unit == 'hours':
            result = self.base_time - datetime.timedelta(hours=delta)
        else:
            raise ValueError("Unsupported time unit. Use 'seconds', 'minutes', or 'hours'.")
        return result
    def get_time_difference(self, end_time, start_time):
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise TypeError("Both start_time and end_time must be datetime objects.")
        if start_time > end_time:
            return -1                                                                      
        difference = end_time - start_time
        return difference
if __name__ == '__main__':
    start = datetime.datetime(2023, 10, 26, 10, 0, 0)
    calculator = TimeCalculator(base_time=start)
    print(f"Base Time: {start}")
    try:
        time_plus_minutes = calculator.add_time(30, unit='minutes')
        print(f"Time + 30 minutes: {time_plus_minutes}")
        time_plus_hours = calculator.add_time(2, unit='hours')
        print(f"Time + 2 hours: {time_plus_hours}")
        time_minus_seconds = calculator.subtract_time(60, unit='seconds')
        print(f"Time - 60 seconds: {time_minus_seconds}")
        end = datetime.datetime(2023, 10, 26, 11, 30, 0)
        diff = calculator.get_time_difference(end, start)
        print(f"Difference between start and end: {diff}")
        try:
            calculator.add_time(10, unit='days')
        except ValueError as e:
            print(f"Caught expected error: {e}")
        try:
            calculator.add_time(10, unit='weeks')
        except ValueError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")