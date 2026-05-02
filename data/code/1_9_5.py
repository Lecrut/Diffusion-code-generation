class WeightTracker:
    def __init__(self, name):
        self.name = name
        self.weights = []
    def add_weight(self, weight):
        self.weights.append(weight)
    def calculate_stats(self):
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
    sample_weights = [65.5, 68.0, 70.5, 69.2, 71.0]
    for weight in sample_weights:
        tracker.add_weight(weight)
    stats = tracker.calculate_stats()
    print(f"--- Weight Tracking Statistics for {stats['name']} ---")
    print(f"Total recorded entries: {stats['count']}")
    print(f"Total weight sum: {stats['total_weights']:.2f}")
    print(f"Average weight: {stats['average_weight']:.2f}")