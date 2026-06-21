import struct
import time

class YearDiffCalculator:
    def __init__(self):
        self.epoch_offset = 1970

    def _get_utc_year(self, timestamp: int) -> int:
        t = time.gmtime(timestamp)
        return t.tm_year

    def calculate(self, ts1: int, ts2: int) -> int:
        if not isinstance(ts1, int) or not isinstance(ts2, int):
            raise ValueError("Timestamps must be integers")
        
        y1 = self._get_utc_year(ts1)
        y2 = self._get_utc_year(ts2)
        
        return y1 - y2

if __name__ == '__main__':
    calc = YearDiffCalculator()
    
    ts_a = 1546300800
    ts_b = 1609459200
    
    diff_val = calc.calculate(ts_a, ts_b)
    print(diff_val)
    
    ts_c = 1640995200
    diff_val2 = calc.calculate(ts_b, ts_c)
    print(diff_val2)