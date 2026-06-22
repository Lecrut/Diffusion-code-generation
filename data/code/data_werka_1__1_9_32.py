class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
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
        return min(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(70.5)
    tracker.add_weight(68.2)
    tracker.add_weight(72.3)
    
    print("Average Weight:", tracker.get_average_weight())
    print("Max Weight:", tracker.get_max_weight())
    print("Min Weight:", tracker.get_min_weight())