import datetime

class TimeElapsedCalculator:
    @staticmethod
    def get_current_time():
        return datetime.datetime.now()

    @staticmethod
    def get_start_of_day(time):
        return time.replace(hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def calculate_elapsed_time(cls):
        current_time = cls.get_current_time()
        start_of_day = cls.get_start_of_day(current_time)
        elapsed_time = current_time - start_of_day
        return elapsed_time

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    elapsed_time = calculator.calculate_elapsed_time()
    print(f"Time elapsed today: {elapsed_time}")