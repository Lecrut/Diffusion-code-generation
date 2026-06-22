class WeightData:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be numeric")
        if value <= 0:
            raise ValueError("Weight must be positive")
        self.value = value

class WeightTracker:
    def __init__(self):
        self._history = []
        self._baseline = None

    def set_baseline(self, weight):
        data = WeightData(weight)
        self._baseline = data.value

    def log_entry(self, weight):
        data = WeightData(weight)
        self._history.append(data.value)
        return len(self._history)

    def get_current_stats(self):
        if not self._history:
            return {
                "entries": 0,
                "latest": None,
                "change_from_baseline": None,
                "min": None,
                "max": None,
                "average": None
            }
        
        current = self._history[-1]
        total = sum(self._history)
        count = len(self._history)
        average = total / count
        minimum = min(self._history)
        maximum = max(self._history)
        
        baseline_diff = None
        if self._baseline is not None:
            baseline_diff = current - self._baseline
        
        return {
            "entries": count,
            "latest": current,
            "change_from_baseline": baseline_diff,
            "min": minimum,
            "max": maximum,
            "average": average
        }

def run_simulation():
    tracker = WeightTracker()
    tracker.set_baseline(80.0)
    
    tracker.log_entry(79.5)
    tracker.log_entry(79.2)
    tracker.log_entry(78.8)
    tracker.log_entry(79.0)
    
    final_stats = tracker.get_current_stats()
    print(f"Total entries: {final_stats['entries']}")
    print(f"Latest weight: {final_stats['latest']}")
    print(f"Change from baseline: {final_stats['change_from_baseline']}")
    print(f"Average weight: {final_stats['average']}")
    print(f"Minimum weight: {final_stats['min']}")
    print(f"Maximum weight: {final_stats['max']}")

if __name__ == '__main__':
    run_simulation()