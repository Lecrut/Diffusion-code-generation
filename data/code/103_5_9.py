import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()
    _units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }

    @classmethod
    def get_elapsed_time(cls, unit='seconds'):
        with cls._lock:
            now = time.localtime()
            midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
            elapsed_seconds = (time.mktime(now) - time.mktime(midnight)) % 86400
            return int(elapsed_seconds * cls._units.get(unit, 1))

if __name__ == '__main__':
    print(ElapsedTime.get_elapsed_time())