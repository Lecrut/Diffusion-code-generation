class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def get_average_weight(self):
        return sum(self.weights) / len(self.weights) if self.weights else 0

    def get_max_weight(self):
        return max(self.weights) if self.weights else None

    def get_min_weight(self):
        return min(self.weights) if self.weights else None

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [65.4, 71.2, 68.9, 70.1]
    for weight in sample_weights:
        tracker.add_weight(weight)
    
    print("Average Weight:", tracker.get_average_weight())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())