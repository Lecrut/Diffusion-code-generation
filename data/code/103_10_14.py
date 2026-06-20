from datetime import datetime

class TimeSinceMidnight:
    def __init__(self):
        self.today = datetime(2023, 4, 1)
    
    def get_elapsed_time(self):
        now = datetime.now()
        midnight = self.today.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_time = now - midnight
        return elapsed_time

if __name__ == '__main__':
    time_since_midnight = TimeSinceMidnight()
    print(time_since_midnight.get_elapsed_time())