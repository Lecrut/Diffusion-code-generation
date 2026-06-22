class WeightTracker:
    MIN_VALID_WEIGHT = 0

    def __init__(self):
        self.weights = []

    @staticmethod
    def validate_weight(weight):
        if weight < WeightTracker.MIN_VALID_WEIGHT:
            raise ValueError("Weight cannot be negative")

    def add_weight(self, weight):
        WeightTracker.validate_weight(weight)
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

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [75.0, 80.2, 79.5, 81.3]
    for weight in sample_weights:
        tracker.add_weight(weight)
    
    print("Average Weight:", tracker.get_average_weight())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())