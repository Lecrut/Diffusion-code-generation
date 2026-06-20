class WeightTracker:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "count": 0,
                "min": None,
                "max": None,
                "average": None,
                "last": None,
                "total": 0
            }
        
        count = len(self.weights)
        total = sum(self.weights)
        average = total / count
        min_val = min(self.weights)
        max_val = max(self.weights)
        last_val = self.weights[-1]

        return {
            "count": count,
            "min": min_val,
            "max": max_val,
            "average": round(average, 2),
            "last": last_val,
            "total": total
        }

    def get_history(self):
        return list(self.weights)

if __name__ == '__main__':
    tracker = WeightTracker()
    tracker.add_weight(150)
    tracker.add_weight(148)
    tracker.add_weight(145)
    tracker.add_weight(147)
    
    stats = tracker.get_statistics()
    print(f"Total Weights Recorded: {stats['count']}")
    print(f"Starting Weight: {tracker.weights[0]}")
    print(f"Current Weight: {stats['last']}")
    print(f"Lowest Weight: {stats['min']}")
    print(f"Highest Weight: {stats['max']}")
    print(f"Average Weight: {stats['average']}")
    print(f"Total Weight Loss: {stats['total']}")