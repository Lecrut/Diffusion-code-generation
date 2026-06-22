import time
import calendar

class TimeElapsedCalculator:
    def __init__(self, timestamp=None):
        if timestamp is None:
            self.current_time = time.time()
        else:
            self.current_time = timestamp

    def get_seconds_since_midnight(self):
        current_time_struct = time.localtime(self.current_time)
        day_start_timestamp = calendar.timegm(current_time_struct[:9])
        return self.current_time - day_start_timestamp

    def get_current_hour(self):
        return time.localtime(self.current_time).tm_hour

    def get_current_minute(self):
        return time.localtime(self.current_time).tm_min

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    elapsed_seconds = calculator.get_seconds_since_midnight()
    print(elapsed_seconds)
    print(calculator.get_current_hour())
    print(calculator.get_current_minute())