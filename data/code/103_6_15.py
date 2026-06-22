import time

class TimeElapsedCalculator:
    def __init__(self):
        self.epoch_offset = 24 * 3600

    def get_current_timestamp(self):
        return time.time()

    def get_seconds_since_midnight(self):
        current_ts = self.get_current_timestamp()
        seconds_today = current_ts % self.epoch_offset
        return seconds_today

    def format_elapsed_time(self):
        seconds = self.get_seconds_since_midnight()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

if __name__ == '__main__':
    calculator = TimeElapsedCalculator()
    raw_seconds = calculator.get_seconds_since_midnight()
    formatted_time = calculator.format_elapsed_time()
    print(raw_seconds)
    print(formatted_time)