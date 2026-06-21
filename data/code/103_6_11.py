import time

class TimeCalculator:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    @staticmethod
    def _get_local_time_components(timestamp):
        return time.localtime(timestamp)

    def get_seconds_elapsed_today(self, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        local_time = self._get_local_time_components(timestamp)
        hours = local_time.tm_hour
        minutes = local_time.tm_min
        seconds = local_time.tm_sec
        total_seconds = (hours * self.SECONDS_IN_HOUR) + (minutes * self.SECONDS_IN_MINUTE) + seconds
        return total_seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.get_seconds_elapsed_today()
    print(result)