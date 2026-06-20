import datetime

class TimeElapsedCalculator:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def calculate_elapsed(self):
        current_time = datetime.datetime.now()
        elapsed_time = current_time - self.start_time
        return elapsed_time.total_seconds()

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    print(f"Time elapsed since start: {calculator.calculate_elapsed()} seconds")