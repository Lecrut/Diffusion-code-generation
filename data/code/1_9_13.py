class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive")
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

    def get_median(self):
        if not self.weights:
            return None
        sorted_weights = sorted(self.weights)
        n = len(sorted_weights)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_weights[mid - 1] + sorted_weights[mid]) / 2.0
        else:
            return sorted_weights[mid]

    def get_statistics(self):
        if not self.weights:
            return {"count": 0, "average": 0.0, "min": None, "max": None, "median": None}
        return {
            "count": len(self.weights),
            "average": self.get_average(),
            "min": self.get_min(),
            "max": self.get_max(),
            "median": self.get_median()
        }

if __name__ == "__main__":
    tracker = WeightTracker()
    sample_weights = [70.5, 72.3, 71.8, 73.1, 70.9, 72.0]
    for w in sample_weights:
        tracker.add_weight(w)
    stats = tracker.get_statistics()
    print(stats["count"])
    print(round(stats["average"], 2))
    print(stats["min"])
    print(stats["max"])
    print(round(stats["median"], 2))