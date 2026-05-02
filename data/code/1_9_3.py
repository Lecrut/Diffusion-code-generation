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
    tracker.add_weight(65.5)
    tracker.add_weight(70.0)
    tracker.add_weight(68.5)
    tracker.add_weight(72.0)
    stats = tracker.calculate_statistics()
    print(f"--- Weight Tracking Statistics for {stats['name']} ---")
    print(f"Total Weights Recorded: {stats['total_weights']}")
    print(f"Average Weight: {stats['average_weight']:.2f}")
    print(f"Highest Weight: {stats['highest_weight']:.1f}")
    print(f"Lowest Weight: {stats['lowest_weight']:.1f}")