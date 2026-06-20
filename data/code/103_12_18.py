from datetime import datetime

class TimeElapsedCalculator:
    @staticmethod
    def get_time_elapsed_since_midnight():
        current_time = datetime.now()
        start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed_time = current_time - start_of_day
        return elapsed_time

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    elapsed = calculator.get_time_elapsed_since_midnight()
    print(f"{elapsed.seconds // 3600} hours, {(elapsed.seconds % 3600) // 60} minutes, and {elapsed.seconds % 60} seconds")