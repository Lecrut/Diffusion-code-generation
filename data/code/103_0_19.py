from datetime import datetime

class TimeElapsed:
    def __init__(self):
        self.now = datetime.now()
        self.midnight = self.now.replace(hour=0, minute=0, second=0, microsecond=0)

    def calculate_elapsed_seconds(self):
        return (self.now - self.midnight).total_seconds()

if __name__ == '__main__':
    time_instance = TimeElapsed()
    print(time_instance.calculate_elapsed_seconds())