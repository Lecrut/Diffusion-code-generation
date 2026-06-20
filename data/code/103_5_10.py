import time
from threading import Lock

class ElapsedTime:
    _lock = Lock()
    
    @classmethod
    def get_elapsed_time(cls):
        with cls._lock:
            current_time = time.localtime()
            midnight = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, 0, 0, 0))
            elapsed_seconds = (time.mktime(current_time) - time.mktime(midnight)) % 86400
            return elapsed_seconds

if __name__ == '__main__':
    print(ElapsedTime.get_elapsed_time())