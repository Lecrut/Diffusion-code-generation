class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        self.weights.append(weight)

    def get_weights(self):
        return list(self.weights)

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

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "average": 0.0,
                "min": None,
                "max": None,
                "range": 0.0
            }
        min_val = self.get_min()
        max_val = self.get_max()
        return {
            "count": len(self.weights),
            "average": self.get_average(),
            "min": min_val,
            "max": max_val,
            "range": max_val - min_val
        }

    def clear(self):
        self.weights = []

def main():
    tracker = WeightTracker()
    sample_weights = [70.5, 69.8, 71.2, 70.0, 69.5, 70.8, 71.5]
    for w in sample_weights:
        tracker.add_weight(w)
    
    stats = tracker.get_statistics()
    print(stats)

if __name__ == '__main__':
    main()