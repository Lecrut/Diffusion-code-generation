class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights.append(weight)

    def get_stats(self):
        if not self.weights:
            return {"count": 0, "min": None, "max": None, "average": None, "total": 0}
        return {
            "count": len(self.weights),
            "min": min(self.weights),
            "max": max(self.weights),
            "average": sum(self.weights) / len(self.weights),
            "total": sum(self.weights)
        }

    def display_stats(self):
        stats = self.get_stats()
        print(f"Entries: {stats['count']}")
        print(f"Min: {stats['min']}")
        print(f"Max: {stats['max']}")
        print(f"Average: {stats['average']:.2f}")
        print(f"Total: {stats['total']}")

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(70.5)
    tracker.add_weight(72.0)
    tracker.add_weight(68.5)
    tracker.add_weight(75.0)
    tracker.display_stats()
    print(tracker.get_stats()['average'])