class MetricData:
    def __init__(self):
        self.entries = []

    def record(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        if value <= 0:
            raise ValueError("Value must be positive")
        self.entries.append(value)

    def calculate_aggregates(self):
        if not self.entries:
            return {
                "count": 0,
                "sum": 0.0,
                "mean": 0.0,
                "lowest": None,
                "highest": None
            }
        total = sum(self.entries)
        count = len(self.entries)
        return {
            "count": count,
            "sum": total,
            "mean": total / count,
            "lowest": min(self.entries),
            "highest": max(self.entries)
        }

    def get_entries(self):
        return list(self.entries)

def run_demonstration():
    tracker = MetricData()
    tracker.record(75.5)
    tracker.record(74.2)
    tracker.record(76.8)
    tracker.record(73.1)
    results = tracker.calculate_aggregates()
    print(results)

if __name__ == '__main__':
    run_demonstration()