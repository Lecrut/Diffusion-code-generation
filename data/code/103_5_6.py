import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()

    @classmethod
    def get_elapsed_time(cls):
        with cls._lock:
            now = time.localtime()
            midnight = cls.calculate_midnight(now)
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return int(elapsed_seconds)

    @staticmethod
    def calculate_midnight(time_struct):
        return time.struct_time((time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday, 0, 0, 0, time_struct.tm_wday, time_struct.tm_yday, time_struct.tm_isdst))

if __name__ == '__main__':
    elapsed = ElapsedTime.get_elapsed_time()
    print(f"Elapsed time since midnight: {elapsed} seconds")