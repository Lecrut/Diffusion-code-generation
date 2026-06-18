class WeightTracker:
    def __init__(self):
        self._weights = []  # Internal list to store recorded weights (private by convention)

    @property
    def total_weight(self) -> float:
        """Returns the sum of all recorded weights."""
        return sum(self._weights) if self._weights else 0.0

    @property
    def average_weight(self) -> float:
        """Returns the arithmetic mean of all recorded weights."""
        if not self._weights:
            return 0.0
        return self.total_weight / len(self._weights)

    @property
    def min_weight(self) -> float | None:
        """Returns the minimum weight recorded, or None if no data exists."""
        if not self._weights:
            return None
        return min(self._weights)

    @property
    def max_weight(self) -> float | None:
        """Returns the maximum weight recorded, or None if no data exists."""
        if not self._weights:
            return None
        return max(self._weights)

    @property
    def count(self) -> int:
        """Returns the number of weights currently tracked."""
        return len(self._weights)

    def add_weight(self, weight: float) -> bool:
        """Adds a new weight to the tracking system. Returns True on success."""
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number.")
        
        self._weights.append(weight)
        return True

    def get_statistics(self) -> dict[str, any]:
        """Returns a dictionary containing all current statistics."""
        return {
            "total": round(self.total_weight, 2),
            "average": round(self.average_weight, 2),
            "min": self.min_weight if self._weights else None,
            "max": self.max_weight if self._weights else None,
            "count": self.count
        }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    tracker = WeightTracker()

    # Simulate adding initial weights based on a list of sample data points
    sample_entries: list[float] = [65.0, 72.3, 81.4, 90.2, 88.5]
    
    for entry in sample_entries:
        tracker.add_weight(entry)

    # Display the results immediately after initialization with samples
    stats = tracker.get_statistics()
    print("Weight Tracking System Statistics")
    print("-" * 30)
    print(f"Total Weight: {stats['total']} kg")
    print(f"Average Weight: {stats['average']} kg")
    print(f"Minimum Weight: {stats['min']} kg")
    print(f"Maximum Weight: {stats['max']} kg")
    print(f"Number of Entries: {stats['count']}")

    # Simulate adding a new weight to show update capability (still no user input)
    tracker.add_weight(95.0)
    
    updated_stats = tracker.get_statistics()
    print("-" * 30)
    print("Updated Statistics after New Entry:")
    print(f"Total Weight: {updated_stats['total']} kg")
    print(f"Average Weight: {updated_stats['average']} kg")