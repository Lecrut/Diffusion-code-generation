from datetime import datetime

class TimeCalculator:
    def __init__(self):
        self.now = datetime.now()
    
    @property
    def seconds_since_midnight(self):
        start_of_day = datetime(self.now.year, self.now.month, self.now.day)
        return (self.now - start_of_day).total_seconds()

if __name__ == '__main__':
    calculator = TimeCalculator()
    print(f"Seconds elapsed since midnight: {calculator.seconds_since_midnight}")