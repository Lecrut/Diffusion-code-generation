class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        self.weights.append(weight)

    def get_count(self):
        return len(self.weights)

    def get_mean(self):
        if not self.weights:
            return 0.0
        return sum(self.weights) / len(self.weights)

    def get_median(self):
        if not self.weights:
            return 0.0
        sorted_weights = sorted(self.weights)
        n = len(sorted_weights)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_weights[mid - 1] + sorted_weights[mid]) / 2.0
        else:
            return float(sorted_weights[mid])

    def get_min(self):
        if not self.weights:
            return 0.0
        return min(self.weights)

    def get_max(self):
        if not self.weights:
            return 0.0
        return max(self.weights)

    def get_statistics(self):
        return {
            "count": self.get_count(),
            "mean": self.get_mean(),
            "median": self.get_median(),
            "min": self.get_min(),
            "max": self.get_max()
        }

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 71.2, 69.8, 72.1, 70.0, 71.5, 70.8]
    for w in sample_weights:
        tracker.add_weight(w)
    stats = tracker.get_statistics()
    print(stats)