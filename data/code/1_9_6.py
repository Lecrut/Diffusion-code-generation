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
                "highest_weight": 0,
                "lowest_weight": 0
            }
        total = sum(self.weights)
        average = total / len(self.weights)
        highest = max(self.weights)
        lowest = min(self.weights)
        return {
            "name": self.name,
            "total_weights": total,
            "average_weight": average,
            "highest_weight": highest,
            "lowest_weight": lowest
        }
if __name__ == '__main__':
    tracker = WeightTracker("Alice")
    sample_weights = [65.5, 68.0, 70.5, 66.0, 72.5]
    for weight in sample_weights:
        tracker.add_weight(weight)
    statistics = tracker.calculate_statistics()
    print(f"--- Weight Tracking Statistics for {statistics['name']} ---")
    print(f"Total Weights Recorded: {statistics['total_weights']}")
    print(f"Average Weight: {statistics['average_weight']:.2f}")
    print(f"Highest Weight: {statistics['highest_weight']:.2f}")
    print(f"Lowest Weight: {statistics['lowest_weight']:.2f}")