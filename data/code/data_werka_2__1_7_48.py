class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def calculate_average(self):
        return self._calculate_statistic(lambda w: sum(w) / len(w))

    def get_max_weight(self):
        return self._calculate_statistic(max)

    def get_min_weight(self):
        return self._calculate_statistic(min)

    def _calculate_statistic(self, func):
        if not self.weights:
            return None
        return func(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [80.2, 75.6, 82.4, 79.9]
    for weight in sample_weights:
        tracker.add_weight(weight)

    print("Average Weight:", tracker.calculate_average())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())