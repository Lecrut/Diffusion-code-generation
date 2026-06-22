class TimeElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, current_hour, current_minute, current_second):
        self.current_hour = current_hour
        self.current_minute = current_minute
        self.current_second = current_second

    def calculate_elapsed_time(self):
        total_seconds = (self.current_hour * self.SECONDS_PER_HOUR +
                         self.current_minute * self.SECONDS_PER_MINUTE +
                         self.current_second)
        hours = total_seconds // self.SECONDS_PER_HOUR
        remaining_seconds = total_seconds % self.SECONDS_PER_HOUR
        minutes = remaining_seconds // self.SECONDS_PER_MINUTE
        seconds = remaining_seconds % self.SECONDS_PER_MINUTE
        return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    calculator = TimeElapsedCalculator(10, 30, 45)
    result = calculator.calculate_elapsed_time()
    print(result)