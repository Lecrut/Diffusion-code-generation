import time

class TimeCalculator:
    SECONDS_IN_DAY = 86400

    @staticmethod
    def get_seconds_since_start_of_day():
        current_time = time.time()
        start_of_day = current_time - (current_time % 86400)
        return current_time - start_of_day

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.get_seconds_since_start_of_day()
    print(result)