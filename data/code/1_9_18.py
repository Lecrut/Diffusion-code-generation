class WeightTracker:
    def __init__(self, name):
        self.name = name
        self.weights = []

    def add_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.weights.append(weight)

    def get_statistics(self):
        if not self.weights:
            return {
                "name": self.name,
                "count": 0,
                "latest": None,
                "min": None,
                "max": None,
                "average": None
            }
        
        current_count = len(self.weights)
        latest_weight = self.weights[-1]
        min_weight = min(self.weights)
        max_weight = max(self.weights)
        average_weight = sum(self.weights) / current_count
        
        return {
            "name": self.name,
            "count": current_count,
            "latest": latest_weight,
            "min": min_weight,
            "max": max_weight,
            "average": round(average_weight, 2)
        }

    def get_trend(self):
        if len(self.weights) < 2:
            return "No trend data available"
        
        first = self.weights[0]
        last = self.weights[-1]
        
        if last > first:
            return "Gaining weight"
        elif last < first:
            return "Losing weight"
        else:
            return "Stable weight"

if __name__ == '__main__':
    tracker = WeightTracker("User_A")
    tracker.add_weight(150.0)
    tracker.add_weight(149.5)
    tracker.add_weight(148.0)
    tracker.add_weight(148.2)
    
    stats = tracker.get_statistics()
    print(f"Tracker: {stats['name']}")
    print(f"Entries: {stats['count']}")
    print(f"Latest: {stats['latest']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Average: {stats['average']}")
    
    trend = tracker.get_trend()
    print(f"Trend: {trend}")