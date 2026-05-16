class WeightTracker:
    def __init__(self):
        self.weights = []
    def add_weight(self, weight):
        self.weights.append(weight)
    def calculate_average(self):
        if not self.weights:
            return 0
        return sum(self.weights) / len(self.weights)
    def calculate_total(self):
        return sum(self.weights)
if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 71.2, 69.8, 72.0, 70.1]
    for weight in sample_weights:
        tracker.add_weight(weight)
    average = tracker.calculate_average()
    total = tracker.calculate_total()
    print(f"Weight Tracking System Simulation")
    print("---------------------------------")
    print(f"Recorded Weights: {tracker.weights}")
    print(f"Total Weight: {total:.2f}")
    print(f"Average Weight: {average:.2f}")