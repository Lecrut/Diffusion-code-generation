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
        return self._calculate_average()

    def get_max_weight(self):
        if not self.weights:
            return None
        return max(self.weights)

    def get_min_weight(self):
        if not self.weights:
            return None
        return min(self.weights)

    def _is_valid_weight(self, weight):
        return isinstance(weight, (int, float)) and weight > 0

    def _calculate_average(self):
        total_weight = sum(self.weights)
        number_of_weights = len(self.weights)
        return total_weight / number_of_weights

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [75.3, 82.1, 69.4, 78.0]
    for weight in sample_weights:
        tracker.add_weight(weight)

    print("Average Weight:", tracker.get_average_weight())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())