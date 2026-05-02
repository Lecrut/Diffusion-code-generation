class WeightTracker:
    def __init__(self, name):
        self.name = name
        self.weights = []
    def add_weight(self, weight):
        self.weights.append(weight)
    def calculate_statistics(self):
        if not self.weights:
            return {
                "name": self.name,
                "total_weights": 0,
                "average_weight": 0,
                "count": 0
            }
        total = sum(self.weights)
        count = len(self.weights)
        average = total / count
        return {
            "name": self.name,
            "total_weights": total,
            "average_weight": average,
            "count": count
        }
if __name__ == '__main__':
    tracker = WeightTracker("Alice")
    sample_weights = [65.5, 68.0, 70.5, 72.0, 69.5]
    for weight in sample_weights:
        tracker.add_weight(weight)
    statistics = tracker.calculate_statistics()
    print(f"--- Weight Tracking Statistics for {statistics['name']} ---")
    print(f"Total number of entries: {statistics['count']}")
    print(f"Total weight recorded: {statistics['total_weights']:.2f}")
    print(f"Average weight: {statistics['average_weight']:.2f}")