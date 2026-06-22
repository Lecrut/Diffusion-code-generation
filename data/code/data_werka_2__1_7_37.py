class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not self._is_valid_weight(weight):
            raise ValueError("Weight must be a positive number")
        self.weights.append(weight)

    def get_average_weight(self):
        if not self.weights:
            return 0
        return sum(self.weights) / len(self.weights)

    def get_max_weight(self):
        if not self.weights:
            return None
        return max(self.weights)

    def get_min_weight(self):
        if not self.weights:
            return None

    def _is_valid_weight(self, weight):
        return isinstance(weight, (int, float)) and weight > 0

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 68.2, 72.3, 69.8]
    for weight in sample_weights:
        tracker.add_weight(weight)

    print("Average Weight:", tracker.get_average_weight())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())