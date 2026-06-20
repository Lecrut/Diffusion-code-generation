from datetime import datetime

class TimeCalculator:
    def __init__(self):
        self.now = datetime.now()
    
    def get_start_of_day(self):
        return self.now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    def calculate_elapsed_seconds(self):
        start_of_day = self.get_start_of_day()
        elapsed_seconds = (self.now - start_of_day).total_seconds()
        return int(elapsed_seconds)

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed_time = calculator.calculate_elapsed_seconds()
    print(elapsed_time)