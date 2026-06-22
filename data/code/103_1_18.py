class TimeElapsedCalculator:
    def __init__(self):
        self._ms_per_sec = 1000
        self._secs_per_min = 60
        self._mins_per_hour = 60

    def calculate_elapsed_ms(self):
        import time
        now = time.localtime()
        h = now.tm_hour
        m = now.tm_min
        s = now.tm_sec
        ms = now.tm_msec
        
        total_secs = (h * self._mins_per_hour * self._secs_per_min) + (m * self._secs_per_min) + s
        total_ms = (total_secs * self._ms_per_sec) + ms
        return total_ms

    def get_component_breakdown(self):
        import time
        now = time.localtime()
        return {
            "hours": now.tm_hour,
            "minutes": now.tm_min,
            "seconds": now.tm_sec,
            "milliseconds": now.tm_msec
        }

if __name__ == '__main__':
    calc = TimeElapsedCalculator()
    ms_result = calc.calculate_elapsed_ms()
    print(ms_result)
    
    breakdown = calc.get_component_breakdown()
    print(breakdown["hours"] * 3600000 + breakdown["minutes"] * 60000 + breakdown["seconds"] * 1000 + breakdown["milliseconds"])