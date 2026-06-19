class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        self.weights.append(weight)

    def get_min_weight(self):
        return min(self.weights) if self.weights else None

    def get_max_weight(self):
        return max(self.weights) if self.weights else None

    def get_average_weight(self):
        return sum(self.weights) / len(self.weights) if self.weights else None

    def get_weight_count(self):
        return len(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 68.2, 72.3, 69.8, 71.4]
    for weight in sample_weights:
        tracker.add_weight(weight)
    
    print("Minimum Weight:", tracker.get_min_weight())
    print("Maximum Weight:", tracker.get_max_weight())
    print("Average Weight:", tracker.get_average_weight())
    print("Weight Count:", tracker.get_weight_count())