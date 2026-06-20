import time

class TimeUtils:
    EPOCH = time.mktime((1970, 1, 1, 0, 0, 0, 0, 0, -1))
    
    @staticmethod
    def get_midnight_timestamp():
        now = time.time()
        midnight = time.mktime(time.localtime(now))
        return int(midnight)
    
    @classmethod
    def seconds_elapsed_today(cls):
        now = time.time()
        midnight = cls.get_midnight_timestamp()
        return int(now - midnight)

if __name__ == '__main__':
    elapsed_seconds = TimeUtils.seconds_elapsed_today()
    print(elapsed_seconds)