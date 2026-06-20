import time

class TimeElapsed:
    def __init__(self):
        self.now = time.localtime()
    
    def elapsed_seconds_today(self):
        return (self.now.tm_hour * 3600) + (self.now.tm_min * 60) + self.now.tm_sec

if __name__ == '__main__':
    te = TimeElapsed()
    print(f"Elapsed seconds today: {te.elapsed_seconds_today()}")