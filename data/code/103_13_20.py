import time

class DayFractionCalculator:
    SECONDS_PER_HOUR = 3600
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    SECONDS_PER_DAY = HOURS_PER_DAY * SECONDS_PER_HOUR

    @staticmethod
    def _get_current_time_struct():
        return time.localtime()

    def calculate_fraction(self):
        time_struct = self._get_current_time_struct()
        hours = time_struct.tm_hour
        minutes = time_struct.tm_min
        seconds = time_struct.tm_sec
        milliseconds = time_struct.tm_sec % 1
        total_elapsed_seconds = (hours * self.SECONDS_PER_HOUR) + (minutes * self.MINUTES_PER_HOUR) + seconds + milliseconds
        fraction = total_elapsed_seconds / self.SECONDS_PER_DAY
        return fraction

if __name__ == '__main__':
    calculator = DayFractionCalculator()
    result = calculator.calculate_fraction()
    print(result)