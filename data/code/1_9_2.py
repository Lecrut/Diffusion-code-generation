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
                "total_weight": 0,
                "average_weight": 0,
                "count": 0
            }
        total_weight = sum(self.weights)
        count = len(self.weights)
        average_weight = total_weight / count
        return {
            "name": self.name,
            "total_weight": total_weight,
            "average_weight": average_weight,
            "count": count
        }
if __name__ == '__main__':
    tracker = WeightTracker("Alice")
    sample_weights = [65.5, 66.0, 65.8, 67.1, 66.5]
    for weight in sample_weights:
        tracker.add_weight(weight)
    statistics = tracker.calculate_statistics()
    print(f"--- Weight Tracking Statistics for {statistics['name']} ---")
    print(f"Total recorded weights: {statistics['count']}")
    print(f"Total weight: {statistics['total_weight']:.2f}")
    print(f"Average weight: {statistics['average_weight']:.2f}")