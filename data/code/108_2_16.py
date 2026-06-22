import time

class DayCalculator:
    def __init__(self):
        self.reference_time = time.time()

    def get_current_day(self):
        local_time = time.localtime(self.reference_time)
        return local_time.tm_mday

    def get_day_from_timestamp(self, timestamp):
        local_time = time.localtime(timestamp)
        return local_time.tm_mday

if __name__ == '__main__':
    calculator = DayCalculator()
    current_day = calculator.get_current_day()
    print(current_day)
    sample_timestamp = 1697328000.0
    sample_day = calculator.get_day_from_timestamp(sample_timestamp)
    print(sample_day)