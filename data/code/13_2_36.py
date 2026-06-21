from datetime import datetime

class TimeCalculator:
    def __init__(self, timestamps):
        self.timestamps = timestamps

    def calculate_earliest(self):
        return min(datetime.fromisoformat(ts) for ts in self.timestamps)

    def calculate_latest(self):
        return max(datetime.fromisoformat(ts) for ts in self.timestamps)

    def total_elapsed_time(self):
        if not self.timestamps:
            return 0
        earliest = self.calculate_earliest()
        latest = self.calculate_latest()
        return (latest - earliest).total_seconds()

if __name__ == '__main__':
    sample_timestamps = [
        "2023-09-15T08:00:00Z",
        "2023-09-16T17:45:00Z",
        "2023-09-15T14:15:00Z"
    ]
    
    calculator = TimeCalculator(sample_timestamps)
    print("Earliest Timestamp:", calculator.calculate_earliest())
    print("Latest Timestamp:", calculator.calculate_latest())
    print("Total Elapsed Time (seconds):", calculator.total_elapsed_time())