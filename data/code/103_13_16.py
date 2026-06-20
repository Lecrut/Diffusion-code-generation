import time

class DayFractionCalculator:
    SECONDS_IN_DAY = 24 * 60 * 60
    
    @staticmethod
    def get_day_fraction():
        current_time = time.time()
        elapsed_seconds = current_time % DayFractionCalculator.SECONDS_IN_DAY
        day_fraction = elapsed_seconds / DayFractionCalculator.SECONDS_IN_DAY
        return day_fraction

if __name__ == '__main__':
    fraction = DayFractionCalculator.get_day_fraction()
    print(fraction)