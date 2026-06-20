class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number")
        self.weights.append(weight)

    def get_average(self):
        if not self.weights:
            return 0.0
        return sum(self.weights) / len(self.weights)

    def get_min(self):
        if not self.weights:
            return None
        return min(self.weights)

    def get_max(self):
        if not self.weights:
            return None
        return max(self.weights)

    def get_count(self):
        return len(self.weights)

    def get_latest(self):
        if not self.weights:
            return None
        return self.weights[-1]

    def get_stats(self):
        return {
            "count": self.get_count(),
            "latest": self.get_latest(),
            "min": self.get_min(),
            "max": self.get_max(),
            "average": self.get_average()
        }

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(150)
    tracker.add_weight(155)
    tracker.add_weight(152)
    tracker.add_weight(148)
    result = tracker.get_stats()
    print(result)