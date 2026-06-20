import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()

    @classmethod
    def get_current_time(cls):
        return time.localtime()

    @staticmethod
    def is_valid_time_struct(time_struct):
        if not isinstance(time_struct, time.struct_time):
            raise ValueError("Invalid time struct")
        if any(not 0 <= value < max_val for value, max_val in zip(
                (time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday,
                 time_struct.tm_hour, time_struct.tm_min, time_struct.tm_sec),
                (3000, 13, 32, 24, 60, 61))):
            raise ValueError("Invalid time struct values")

    @classmethod
    def calculate_midnight(cls, time_struct):
        cls.is_valid_time_struct(time_struct)
        return time.struct_time((time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday, 0, 0, 0,
                                 time_struct.tm_wday, time_struct.tm_yday, time_struct.tm_isdst))

    @classmethod
    def get_elapsed_seconds(cls):
        with cls._lock:
            now = cls.get_current_time()
            midnight = cls.calculate_midnight(now)
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return int(elapsed_seconds)

if __name__ == '__main__':
    print(ElapsedTime.get_elapsed_seconds())