class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "mean": 0.0,
                "min": 0.0,
                "max": 0.0,
                "latest": 0.0,
                "trend": "stable"
            }

        count = len(self.weights)
        mean = sum(self.weights) / count
        min_w = min(self.weights)
        max_w = max(self.weights)
        latest = self.weights[-1]

        if count >= 2:
            first_half = self.weights[:count // 2]
            second_half = self.weights[count // 2:]
            avg_first = sum(first_half) / len(first_half)
            avg_second = sum(second_half) / len(second_half)
            if avg_second > avg_first * 1.01:
                trend = "increasing"
            elif avg_second < avg_first * 0.99:
                trend = "decreasing"
            else:
                trend = "stable"
        else:
            trend = "stable"

        return {
            "count": count,
            "mean": mean,
            "min": min_w,
            "max": max_w,
            "latest": latest,
            "trend": trend
        }

    def clear_history(self):
        self.weights.clear()

if __name__ == '__main__':
    tracker = WeightTracker()
    sample_weights = [70.5, 71.2, 70.8, 71.5, 72.0, 71.8, 72.3]
    for w in sample_weights:
        tracker.add_weight(w)
    stats = tracker.get_statistics()
    print(stats)