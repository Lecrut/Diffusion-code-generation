from datetime import time

class TimeElapsedCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, current: time):
        if not isinstance(current, time):
            raise TypeError("current must be a datetime.time instance")
        self.current = current

    def _total_seconds(self) -> int:
        return (self.current.hour * self.SECONDS_PER_HOUR +
                self.current.minute * self.SECONDS_PER_MINUTE +
                self.current.second)

    def calculate_elapsed(self) -> dict:
        total = self._total_seconds()
        hours = total // self.SECONDS_PER_HOUR
        remainder = total % self.SECONDS_PER_HOUR
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        return {
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    from datetime import time as dt_time
    sample = dt_time(14, 30, 45)
    calc = TimeElapsedCalculator(sample)
    result = calc.calculate_elapsed()
    print(result)