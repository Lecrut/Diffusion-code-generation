class WeightTracker:
    def __init__(self, initial_weight=None):
        self.weights = []
        if initial_weight is not None:
            self.weights.append(initial_weight)

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "current": None,
                "average": None,
                "min": None,
                "max": None
            }
        return {
            "count": len(self.weights),
            "current": self.weights[-1],
            "average": sum(self.weights) / len(self.weights),
            "min": min(self.weights),
            "max": max(self.weights)
        }

    def get_weight_history(self):
        return list(self.weights)

    def calculate_weight_change(self):
        if len(self.weights) < 2:
            return 0.0
        return self.weights[-1] - self.weights[-2]

if __name__ == '__main__':
    tracker = WeightTracker(180.0)
    tracker.add_weight(178.5)
    tracker.add_weight(179.0)
    tracker.add_weight(177.5)
    
    stats = tracker.get_statistics()
    history = tracker.get_weight_history()
    change = tracker.calculate_weight_change()
    
    print(f"Total entries: {stats['count']}")
    print(f"Current weight: {stats['current']}")
    print(f"Average weight: {stats['average']:.2f}")
    print(f"Weight range: {stats['min']} to {stats['max']}")
    print(f"Last change: {change:.2f}")
    print(f"Full history: {history}")