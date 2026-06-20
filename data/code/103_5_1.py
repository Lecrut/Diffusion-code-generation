import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()

    @classmethod
    def get_elapsed_time(cls):
        with cls._lock:
            now = time.localtime()
            midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return elapsed_seconds

if __name__ == '__main__':
    print(ElapsedTime.get_elapsed_time())