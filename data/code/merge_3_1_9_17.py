import copy

class WeightEntry:
    """Represents a single weight entry with date and value."""
    
    def __init__(self, date_str: str, weight_value: float):
        self.date = date_str
        self.weight = weight_value
    
    @property
    def total_weight(self) -> float:
        return sum(entry.weight for entry in self._entries) if hasattr(self, '_entries') else 0.0

class WeightTracker:
    """Manages a collection of weight entries and calculates statistics."""

    def __init__(self):
        # Initialize with an empty list to store WeightEntry objects
        self.entries = []

    def add_entry(self, date_str: str, weight_value: float) -> None:
        """Adds a new weight entry to the tracker.
        
        Args:
            date_str (str): The string representation of the date.
            weight_value (float): The numerical value of the weight.
        """
        self.entries.append(WeightEntry(date_str, weight_value))

    def get_total_weight(self) -> float:
        """Calculates and returns the sum of all recorded weights."""
        return sum(entry.weight for entry in self.entries) if self.entries else 0.0

    def get_average_weight(self) -> float:
        """Calculates and returns the average weight across all entries."""
        total = self.get_total_weight()
        count = len(self.entries)
        if count == 0:
            return 0.0
        return round(total / count, 2)

    def get_min_weight(self) -> float | None:
        """Returns the minimum weight recorded."""
        if not self.entries:
            return None
        return min(entry.weight for entry in self.entries)

    def get_max_weight(self) -> float | None:
        """Returns the maximum weight recorded."""
        if not self.entries:
            return None
        return max(entry.weight for entry in self.entries)

def run_simulation():
    """Executes a complete simulation with hard-coded sample data.
    
    This function initializes a WeightTracker, adds several entries manually,
    and then prints the updated statistics without requiring user input or 
    external dependencies like files or network access.
    """
    # Initialize tracker instance
    my_tracker = WeightTracker()

    # Hard-coded sample values to simulate adding weights over time
    sample_data = [
        ("2023-10-01", 75.5),
        ("2023-10-08", 74.8),
        ("2023-10-15", 76.2),
        ("2023-10-22", 75.9),
    ]

    # Add entries to the tracker using sample data
    for date, weight in sample_data:
        my_tracker.add_entry(date, weight)

    # Display updated statistics based on the added samples
    print("Weight Tracking System Statistics")
    print("-" * 30)
    
    total = my_tracker.get_total_weight()
    average = my_tracker.get_average_weight()
    minimum = my_tracker.get_min_weight()
    maximum = my_tracker.get_max_weight()

    # Format output for readability, handling None values if no data existed (though sample has data)
    print(f"Total Weight: {total} kg")
    print(f"Average Weight: {average} kg")
    
    if minimum is not None and maximum is not None:
        print(f"Weight Range: {minimum:.2f} kg - {maximum:.2f} kg")

if __name__ == '__main__':
    run_simulation()