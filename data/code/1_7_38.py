class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {"average": 0, "max": None, "min": None}
        
        total_weight = sum(self.weights)
        number_of_weights = len(self.weights)
        average_weight = total_weight / number_of_weights
        max_weight = max(self.weights)
        min_weight = min(self.weights)
        
        return {
            "average": average_weight,
            "max": max_weight,
            "min": min_weight
        }

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 68.2, 72.3, 69.8]
    for weight in sample_weights:
        tracker.add_weight(weight)
    
    stats = tracker.get_statistics()
    print(stats)