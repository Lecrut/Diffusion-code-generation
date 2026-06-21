from datetime import datetime, timedelta
class ElapsedSeconds:
    def __init__(self):
        self.now = datetime.now()
        self.start_of_day = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
    def total_seconds(self):
        return int((self.now - self.start_of_day).total_seconds())
if __name__ == '__main__':
    instance = ElapsedSeconds()
    print(instance.total_seconds())