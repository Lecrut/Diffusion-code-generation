class WeightRecord:
    def __init__(self, date, weight):
        self.date = date
        self.weight = weight

class WeightTracker:
    def __init__(self):
        self.records = []

    def add_weight(self, date, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        record = WeightRecord(date, weight)
        self.records.append(record)
        return record

    def get_average_weight(self):
        if not self.records:
            return 0.0
        total = sum(r.weight for r in self.records)
        return total / len(self.records)

    def get_min_weight(self):
        if not self.records:
            return 0.0
        return min(r.weight for r in self.records)

    def get_max_weight(self):
        if not self.records:
            return 0.0
        return max(r.weight for r in self.records)

    def get_latest_weight(self):
        if not self.records:
            return 0.0
        return self.records[-1].weight

    def get_count(self):
        return len(self.records)

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight("2023-01-01", 75.5)
    tracker.add_weight("2023-01-02", 75.2)
    tracker.add_weight("2023-01-03", 74.8)
    avg = tracker.get_average_weight()
    min_w = tracker.get_min_weight()
    max_w = tracker.get_max_weight()
    latest = tracker.get_latest_weight()
    count = tracker.get_count()
    print(f"Average: {avg}, Min: {min_w}, Max: {max_w}, Latest: {latest}, Count: {count}")