import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()
    
    @classmethod
    def get_current_time(cls):
        return time.localtime()
    
    @classmethod
    def calculate_midnight(cls, time_struct):
        return time.struct_time((time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday, 0, 0, 0, time_struct.tm_wday, time_struct.tm_yday, time_struct.tm_isdst))
    
    @classmethod
    def get_elapsed_seconds(cls):
        with cls._lock:
            now = cls.get_current_time()
            midnight = cls.calculate_midnight(now)
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return int(elapsed_seconds)

if __name__ == '__main__':
    et_instance = ElapsedTime()
    print(et_instance.get_elapsed_seconds())