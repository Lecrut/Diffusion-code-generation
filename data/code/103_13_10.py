import time

class DayFractionCalculator:
    def calculate_fraction(self):
        current_time = time.time()
        start_of_day = time.mktime((current_time // 86400) * 86400)
        elapsed_seconds = current_time - start_of_day
        total_seconds_in_day = 86400
        fraction = elapsed_seconds / total_seconds_in_day
        return fraction

if __name__ == '__main__':
    calculator = DayFractionCalculator()
    fraction = calculator.calculate_fraction()
    print(f"Fraction of the day that has passed: {fraction:.2f}")