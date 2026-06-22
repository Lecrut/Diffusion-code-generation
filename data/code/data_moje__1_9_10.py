class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number.")
        self.weights.append(weight)

    def get_average(self):
        if not self.weights:
            return 0.0
        return sum(self.weights) / len(self.weights)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "average": 0.0,
                "min": 0,
                "max": 0
            }
        return {
            "count": len(self.weights),
            "average": self.get_average(),
            "min": min(self.weights),
            "max": max(self.weights)
        }

    def display_stats(self):
        stats = self.get_statistics()
        print(f"Total Entries: {stats['count']}")
        print(f"Average Weight: {stats['average']:.2f}")
        print(f"Minimum Weight: {stats['min']}")
        print(f"Maximum Weight: {stats['max']}")
        return stats

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(150)
    tracker.add_weight(155)
    tracker.add_weight(149)
    tracker.add_weight(160)
    result = tracker.display_stats()
    print(result)