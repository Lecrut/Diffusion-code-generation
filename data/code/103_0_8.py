from datetime import datetime

class TimeCalculator:
    def __init__(self):
        self.now = datetime.now()

    def get_midnight(self):
        return self.now.replace(hour=0, minute=0, second=0, microsecond=0)

    def calculate_elapsed_seconds(self):
        midnight = self.get_midnight()
        elapsed_time = (self.now - midnight)
        return elapsed_time.total_seconds()

if __name__ == '__main__':
    calculator = TimeCalculator()
    print(calculator.calculate_elapsed_seconds())