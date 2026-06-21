class MillisecondClock:
    def __init__(self):
        self._seconds_per_minute = 60
        self._milliseconds_per_second = 1000
        self._milliseconds_per_minute = self._seconds_per_minute * self._milliseconds_per_second
        self._milliseconds_per_hour = self._milliseconds_per_minute * 60

    def get_elapsed_since_midnight(self):
        import time
        current = time.localtime()
        hours = current.tm_hour
        minutes = current.tm_min
        seconds = current.tm_sec
        milliseconds = current.tm_msec

        if not (0 <= hours <= 23):
            raise ValueError("Invalid hour")
        if not (0 <= minutes <= 59):
            raise ValueError("Invalid minute")
        if not (0 <= seconds <= 59):
            raise ValueError("Invalid second")
        if not (0 <= milliseconds <= 999):
            raise ValueError("Invalid millisecond")

        total = (hours * self._milliseconds_per_hour) + \
                (minutes * self._milliseconds_per_minute) + \
                (seconds * self._milliseconds_per_second) + \
                milliseconds
        return total

    def format_elapsed(self):
        total_ms = self.get_elapsed_since_midnight()
        h = total_ms // 3600000
        remainder = total_ms % 3600000
        m = remainder // 60000
        remainder = remainder % 60000
        s = remainder // 1000
        ms = remainder % 1000
        return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"

if __name__ == '__main__':
    clock = MillisecondClock()
    print(clock.get_elapsed_since_midnight())
    print(clock.format_elapsed())