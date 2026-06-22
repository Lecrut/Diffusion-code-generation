class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def calculate_average(self):
        if not self.weights:
            return 0
        return sum(self.weights) / len(self.weights)

    def find_max_weight(self):
        if not self.weights:
            return None
        return max(self.weights)

    def find_min_weight(self):
        if not self.weights:
            return None

    def get_statistics(self):
        average = self.calculate_average()
        max_weight = self.find_max_weight()
        min_weight = self.find_min_weight()
        return {"average": average, "max": max_weight, "min": min_weight}

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 68.2, 72.3, 69.8]
    for weight in sample_weights:
        tracker.add_weight(weight)

    print(tracker.get_statistics())