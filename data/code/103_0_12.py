from datetime import datetime

class TimeSinceMidnight:
    def __init__(self):
        self.now = datetime.now()
    
    def calculate_elapsed_seconds(self):
        midnight = datetime(self.now.year, self.now.month, self.now.day)
        elapsed_time = self.now - midnight
        return elapsed_time.total_seconds()

if __name__ == '__main__':
    time_calculator = TimeSinceMidnight()
    print(time_calculator.calculate_elapsed_seconds())