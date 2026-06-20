import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()
    
    @classmethod
    def get_midnight_time(cls):
        now = time.localtime()
        return time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    
    @classmethod
    def calculate_elapsed_seconds(cls):
        with cls._lock:
            now = time.localtime()
            midnight = cls.get_midnight_time()
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return int(elapsed_seconds)

if __name__ == '__main__':
    et_instance = ElapsedTime()
    print(f"Elapsed seconds from midnight: {et_instance.calculate_elapsed_seconds()}")