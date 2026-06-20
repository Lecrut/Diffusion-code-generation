import time

class TimeUtils:
    @staticmethod
    def seconds_elapsed_today():
        now = time.time()
        midnight = int(time.mktime((now // 86400) * 86400))
        return int(now - midnight)

if __name__ == '__main__':
    print(TimeUtils.seconds_elapsed_today())