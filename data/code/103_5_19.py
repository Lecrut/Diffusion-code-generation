class TimeElapsedCalculator:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400

    def __init__(self):
        import threading
        self._lock = threading.RLock()

    @staticmethod
    def _get_seconds_in_day(time_struct):
        return (
            time_struct.tm_hour * TimeElapsedCalculator.SECONDS_PER_HOUR
            + time_struct.tm_min * TimeElapsedCalculator.SECONDS_PER_MINUTE
            + time_struct.tm_sec
        )

    def get_elapsed_seconds_from_midnight(self, reference_time=None):
        import time
        import calendar
        
        if reference_time is None:
            reference_time = time.time()
        
        with self._lock:
            utc_time = time.gmtime(reference_time)
            seconds_in_day = TimeElapsedCalculator._get_seconds_in_day(utc_time)
            return float(seconds_in_day)

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    sample_time = 1672531200.0
    result = calculator.get_elapsed_seconds_from_midnight(sample_time)
    print(result)