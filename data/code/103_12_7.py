from datetime import datetime

class TimeElapsedCalculator:
    def __init__(self):
        self.now = datetime.now()
        self.midnight = datetime(self.now.year, self.now.month, self.now.day)

    def calculate_elapsed_time(self):
        elapsed_time = self.now - self.midnight
        return elapsed_time.seconds // 3600, (elapsed_time.seconds % 3600) // 60, elapsed_time.seconds % 60

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    hours, minutes, seconds = calculator.calculate_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")