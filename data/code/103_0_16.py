from datetime import datetime

class TimeElapsedSinceMidnight:
    def __init__(self):
        self.now = datetime.now()
    
    def calculate_elapsed_seconds(self):
        midnight = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_seconds = (self.now - midnight).total_seconds()
        return elapsed_seconds

if __name__ == '__main__':
    time_calculator = TimeElapsedSinceMidnight()
    print(time_calculator.calculate_elapsed_seconds())