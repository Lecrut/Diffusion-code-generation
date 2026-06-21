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
        total_weight = sum(self.weights)
        number_of_weights = len(self.weights)
        return total_weight / number_of_weights

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
    sample_weights = [65.2, 70.5, 80.3, 68.9]
    for weight in sample_weights:
        tracker.add_weight(weight)
    
    print("Average Weight:", tracker.calculate_average())
    print("Max Weight:", tracker.find_max_weight())
    print("Min Weight:", tracker.find_min_weight())