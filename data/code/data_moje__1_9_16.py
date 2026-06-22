class WeightTracker:
    def __init__(self, name):
        self.name = name
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights.append(weight)

    def get_latest(self):
        if not self.weights:
            return None
        return self.weights[-1]

    def get_average(self):
        if not self.weights:
            return 0.0
        return sum(self.weights) / len(self.weights)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "latest": None,
                "average": 0.0,
                "min": None,
                "max": None
            }
        return {
            "count": len(self.weights),
            "latest": self.weights[-1],
            "average": self.get_average(),
            "min": min(self.weights),
            "max": max(self.weights)
        }

    def display_report(self):
        stats = self.get_statistics()
        print(f"Weight Report for {self.name}")
        print(f"Entries: {stats['count']}")
        print(f"Latest: {stats['latest']}")
        print(f"Average: {stats['average']:.2f}")
        print(f"Min: {stats['min']}")
        print(f"Max: {stats['max']}")

if __name__ == '__main__':
    tracker = WeightTracker("Alice")
    tracker.add_weight(150.5)
    tracker.add_weight(148.2)
    tracker.add_weight(149.0)
    tracker.add_weight(147.8)
    tracker.display_report()
    print(tracker.get_latest())
    print(tracker.get_average())