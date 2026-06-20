class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
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

    def get_total(self):
        return sum(self.weights)

    def get_count(self):
        return len(self.weights)

    def get_latest(self):
        if not self.weights:
            return None
        return self.weights[-1]

    def get_statistics(self):
        return {
            "count": self.get_count(),
            "total": self.get_total(),
            "average": self.get_average(),
            "min": self.get_min(),
            "max": self.get_max(),
            "latest": self.get_latest()
        }

def main():
    tracker = WeightTracker()
    sample_weights = [70.5, 71.2, 70.8, 69.9, 70.1, 71.5, 70.3]
    for w in sample_weights:
        tracker.add_weight(w)
    stats = tracker.get_statistics()
    print(stats)

if __name__ == '__main__':
    main()