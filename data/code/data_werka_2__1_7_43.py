class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def calculate_average(self):
        return sum(self.weights) / len(self.weights) if self.weights else 0

    def find_max_weight(self):
        return max(self.weights) if self.weights else None

    def find_min_weight(self):
        return min(self.weights) if self.weights else None

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [85.2, 90.4, 78.6, 88.3]
    for weight in sample_weights:
        tracker.add_weight(weight)

    average_weight = tracker.calculate_average()
    max_weight = tracker.find_max_weight()
    min_weight = tracker.find_min_weight()

    print(f"Average Weight: {average_weight}")
    print(f"Max Weight: {max_weight}")
    print(f"Min Weight: {min_weight}")