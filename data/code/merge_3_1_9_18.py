import copy

class WeightEntry:
    """Represents a single weight entry with date and value."""
    
    def __init__(self, date_str: str, weight_value: float):
        self.date = date_str
        self.weight = weight_value
    
    @property
    def formatted_date(self) -> str:
        return f"{self.date} ({self.weight:.1f} kg)"

class WeightTracker:
    """Manages a collection of weight entries and calculates statistics."""

    def __init__(self):
        self._entries = []  # List to store WeightEntry objects
    
    @property
    def count(self) -> int:
        return len(self._entries)
    
    @property
    def total_weight(self) -> float:
        if not self._entries:
            return 0.0
        return sum(entry.weight for entry in self._entries)
    
    @property
    def average_weight(self) -> float:
        if not self._entries:
            return 0.0
        return round(self.total_weight / len(self._entries), 2)
    
    @property
    def min_weight(self) -> float:
        if not self._entries:
            return None
        return min(entry.weight for entry in self._entries)
    
    @property
    def max_weight(self) -> float:
        if not self._entries:
            return None
        return max(entry.weight for entry in self._entries)

    def add_entry(self, date_str: str, weight_value: float):
        """Adds a new weight entry to the tracker."""
        # Basic validation
        try:
            weight = float(weight_value)
        except ValueError:
            raise ValueError(f"Invalid weight value: {weight_value}. Must be numeric.")

        if date_str and not isinstance(date_str, str):
            raise TypeError("Date must be a string.")

        entry = WeightEntry(date_str, weight)
        self._entries.append(entry)

    def get_entries(self) -> list[WeightEntry]:
        """Returns a copy of the internal entries list to prevent external modification."""
        return copy.deepcopy(self._entries)

    def display_statistics(self):
        """Prints formatted statistics based on current data."""
        if not self._entries:
            print("No weight records available.")
            return
        
        count = len(self._entries)
        
        # Calculate stats for consistency with property access logic, 
        # though properties are more efficient. We recompute here to ensure alignment.
        total = sum(e.weight for e in self._entries)
        min_w = min(e.weight for e in self._entries)
        max_w = max(e.weight for e in self._entries)

        print(f"\n--- Weight Tracking Summary ---")
        print(f"Total Entries: {count}")
        print(f"Minimum Weight: {min_w:.1f} kg")
        print(f"Maximum Weight: {max_w:.1f} kg")
        print(f"Average Weight: {self.average_weight:.2f} kg")
        
        # Display individual entries in reverse chronological order (most recent first)
        sorted_entries = sorted(self._entries, key=lambda x: x.date, reverse=True)
        print("\nRecent Entries:")
        for entry in sorted_entries[:5]:  # Show top 5 most recent
            print(f" - {entry.formatted_date}")

if __name__ == '__main__':
    # Hard-coded sample values to simulate user input without interactive prompts.
    
    tracker = WeightTracker()

    # Sample data: Date (YYYY-MM-DD), Weight in kg
    samples = [
        ("2023-10-05", 78.5),
        ("2023-10-12", 79.0),
        ("2023-10-19", 76.4),
        ("2023-10-26", 77.2),
        ("2023-11-02", 80.1),
    ]

    # Populate the tracker with sample data
    for date, weight in samples:
        tracker.add_entry(date, weight)

    # Display initial statistics
    print("Initial Statistics:")
    tracker.display_statistics()

    # Simulate adding new entries (as if user input was processed later)
    additional_samples = [
        ("2023-11-09", 78.8),
        ("2023-11-16", 75.3),
    ]

    for date, weight in additional_samples:
        tracker.add_entry(date, weight)

    # Display updated statistics
    print("\nUpdated Statistics after new entries:")
    tracker.display_statistics()