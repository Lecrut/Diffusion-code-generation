class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
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
        return min(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 68.2, 72.3, 69.8]
    for weight in sample_weights:
        tracker.add_weight(weight)

    print("Average Weight:", tracker.calculate_average())
    print("Max Weight:", tracker.find_max_weight())
    print("Min Weight:", tracker.find_min_weight())