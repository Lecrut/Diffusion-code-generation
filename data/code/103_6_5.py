import time

class TimeUtils:
    @staticmethod
    def seconds_elapsed_today():
        now = time.time()
        midnight = int(time.mktime(time.localtime(now)))
        return int(now - midnight)

if __name__ == '__main__':
    time_utils = TimeUtils()
    elapsed_seconds = time_utils.seconds_elapsed_today()
    print(elapsed_seconds)