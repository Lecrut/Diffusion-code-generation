import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()
    SECONDS_PER_DAY = 86400

    @classmethod
    def get_elapsed_time(cls):
        with cls._lock:
            now = time.localtime()
            midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % cls.SECONDS_PER_DAY
            return int(elapsed_seconds)

if __name__ == '__main__':
    print(ElapsedTime.get_elapsed_time())