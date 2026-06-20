class TimeCalculator:
    def __init__(self):
        self.start_of_day = time.time()

    def get_elapsed_time(self):
        elapsed_seconds = int(time.time() - self.start_of_day)
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    hours, minutes, seconds = calculator.get_elapsed_time()
    print(f"Elapsed time for the current day: {hours} hours, {minutes} minutes, and {seconds} seconds")