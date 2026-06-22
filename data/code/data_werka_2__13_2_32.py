from datetime import datetime

class TimeCalculator:
    def __init__(self, timestamps):
        self.timestamps = timestamps

    def calculate_total_elapsed_time(self):
        if not self.timestamps:
            return 0
        datetime_objects = [datetime.fromisoformat(ts) for ts in self.timestamps]
        earliest = min(datetime_objects)
        latest = max(datetime_objects)
        total_elapsed_time = (latest - earliest).total_seconds()
        return total_elapsed_time

if __name__ == '__main__':
    sample_timestamps = [
        '2023-11-01T10:00:00Z',
        '2023-11-02T14:45:00Z',
        '2023-11-01T09:15:00Z'
    ]
    time_calculator = TimeCalculator(sample_timestamps)
    total_time = time_calculator.calculate_total_elapsed_time()
    print(total_time)