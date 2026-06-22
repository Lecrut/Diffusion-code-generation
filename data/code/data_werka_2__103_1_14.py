class TimeCalculator:
    SECONDS_PER_MINUTE = 60
    MILLISECONDS_PER_SECOND = 1000
    MILLISECONDS_PER_MINUTE = SECONDS_PER_MINUTE * MILLISECONDS_PER_SECOND
    MILLISECONDS_PER_HOUR = 60 * MILLISECONDS_PER_MINUTE

    @staticmethod
    def compute_ms_from_midnight():
        import time
        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        ms = t.tm_msec
        return h * TimeCalculator.MILLISECONDS_PER_HOUR + m * TimeCalculator.MILLISECONDS_PER_MINUTE + s * TimeCalculator.MILLISECONDS_PER_SECOND + ms

if __name__ == '__main__':
    calc = TimeCalculator()
    print(calc.compute_ms_from_midnight())