import datetime

class TimeElapsedCalculator:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def get_elapsed_time(self):
        current_time = datetime.datetime.now()
        elapsed_time = current_time - self.start_time
        return elapsed_time.total_seconds()

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    print(calculator.get_elapsed_time())