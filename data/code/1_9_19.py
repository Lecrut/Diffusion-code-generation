class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be a positive number")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "min": None,
                "max": None,
                "average": None,
                "latest": None
            }
        return {
            "count": len(self.weights),
            "min": min(self.weights),
            "max": max(self.weights),
            "average": sum(self.weights) / len(self.weights),
            "latest": self.weights[-1]
        }

    def get_weight_history(self):
        return list(self.weights)

def run_sample():
    tracker = WeightTracker()
    sample_weights = [70.5, 71.2, 69.8, 70.1, 72.0]
    for w in sample_weights:
        tracker.add_weight(w)
    stats = tracker.get_statistics()
    history = tracker.get_weight_history()
    return stats, history

if __name__ == '__main__':
    stats, history = run_sample()
    print(stats)
    print(history)