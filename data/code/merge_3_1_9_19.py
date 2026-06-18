import datetime

class WeightEntry:
    """Represents a single weight entry with date and value."""
    
    def __init__(self, date_str: str, weight_value: float):
        self.date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        self.weight = weight_value

    @property
    def display_date(self) -> str:
        return self.date.strftime("%B %d, %Y")

class WeightTracker:
    """Manages a collection of weight entries and calculates statistics."""
    
    def __init__(self):
        # Initialize with sample data as per the requirement for no external files or input
        self._entries = [
            WeightEntry("2023-10-01", 185.5),
            WeightEntry("2023-10-08", 184.2),
            WeightEntry("2023-10-15", 186.0),
        ]

    def add_entry(self, date_str: str, weight_value: float) -> None:
        """Adds a new weight entry to the tracker."""
        self._entries.append(WeightEntry(date_str, weight_value))
    
    @property
    def count(self) -> int:
        return len(self._entries)

    @property
    def total_weight(self) -> float:
        if not self._entries:
            raise ValueError("No entries available to calculate total.")
        return sum(entry.weight for entry in self._entries)

    @property
    def average_weight(self) -> float:
        if not self._entries:
            raise ValueError("No entries available to calculate average.")
        return round(self.total_weight / len(self._entries), 2)

    @property
    def min_weight(self) -> float:
        if not self._entries:
            raise ValueError("No entries available to find minimum weight.")
        return min(entry.weight for entry in self._entries)

    @property
    def max_weight(self) -> float:
        if not self._entries:
            raise ValueError("No entries available to find maximum weight.")
        return max(entry.weight for entry in self._entries)

    def get_entries_sorted_by_date(self):
        """Returns a list of WeightEntry objects sorted by date."""
        return sorted(self._entries, key=lambda x: x.date)

if __name__ == '__main__':
    tracker = WeightTracker()
    
    # Display initial statistics for the hard-coded sample values
    print("=== Initial Statistics ===")
    entries_sorted = tracker.get_entries_sorted_by_date()
    dates_str = [entry.display_date for entry in entries_sorted]

    print(f"Total Entries: {tracker.count}")
    try:
        avg_w = tracker.average_weight
        min_w = tracker.min_weight
        max_w = tracker.max_weight
        total_w = tracker.total_weight
        
        print(f"Average Weight: {avg_w} kg")
        print(f"Minimum Weight: {min_w} kg ({dates_str[0]})")
        print(f"Maximum Weight: {max_w} kg ({dates_str[-1] if dates_str else 'N/A'})")
    except ValueError as e:
        print(e)

    # Simulate adding new entries without user input
    tracker.add_entry("2023-10-22", 185.7)
    tracker.add_entry("2023-10-29", 184.9)

    print("\n=== Updated Statistics ===")
    try:
        avg_w = tracker.average_weight
        min_w = tracker.min_weight
        max_w = tracker.max_weight
        total_w = tracker.total_weight
        
        dates_str_updated = [entry.display_date for entry in entries_sorted] # Re-fetch to ensure order reflects new data if needed, though list is static here. 
        # Actually, let's re-sort properly for the display of updated stats
        latest_entries = tracker.get_entries_sorted_by_date()
        
        print(f"Total Entries: {tracker.count}")
        print(f"Average Weight: {avg_w} kg")
        print(f"Minimum Weight: {min_w} kg ({latest_entries[0].display_date})")
        print(f"Maximum Weight: {max_w} kg ({latest_entries[-1].display_date})")
    except ValueError as e:
        print(e)