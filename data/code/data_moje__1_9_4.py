class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "min": None,
                "max": None,
                "average": None
            }
        count = len(self.weights)
        minimum = min(self.weights)
        maximum = max(self.weights)
        average = sum(self.weights) / count
        return {
            "count": count,
            "min": minimum,
            "max": maximum,
            "average": average
        }

    def get_weight_list(self):
        return list(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(150.5)
    tracker.add_weight(148.2)
    tracker.add_weight(152.0)
    tracker.add_weight(149.7)
    stats = tracker.get_statistics()
    print(f"Count: {stats['count']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Average: {stats['average']}")
    print(f"All Weights: {tracker.get_weight_list()}")