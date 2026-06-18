"""
Weight Tracking System Simulation Module

This module simulates a weight tracking system with clean object-oriented design.
It includes functionality to input new weights, manage historical records, 
and display updated statistics (average, total count, min/max).
The program is self-contained and runs without user interaction or external dependencies.
"""

class WeightRecord:
    """Represents a single weight measurement record."""

    def __init__(self, date_str: str, weight_value: float):
        if not isinstance(weight_value, (int, float)):
            raise ValueError("Weight value must be numeric.")
        
        self.date = date_str.strip()
        self.weight = float(weight_value)

    def get_date(self) -> str:
        return self.date

    def get_weight(self) -> float:
        return self.weight

class WeightStats:
    """Holds calculated statistics for a list of weight records."""

    def __init__(self, record_list: list[WeightRecord]):
        if not isinstance(record_list, list):
            raise TypeError("record_list must be a list.")
        
        # Filter out any non-numeric entries just in case (though constructor validates)
        self.records = [r for r in record_list]

    def calculate_average(self) -> float:
        """Calculate the average weight."""
        if not self.records:
            return 0.0
        
        total_weight = sum(r.get_weight() for r in self.records)
        count = len(self.records)
        return round(total_weight / count, 2)

    def calculate_total_count(self) -> int:
        """Return the number of records."""
        return len(self.records)

    def get_min_weight(self) -> float | None:
        """Get the minimum weight recorded. Returns None if no data."""
        weights = [r.get_weight() for r in self.records]
        return min(weights) if weights else None

    def get_max_weight(self) -> float | None:
        """Get the maximum weight recorded. Returns None if no data."""
        weights = [r.get_weight() for r in self.records]
        return max(weights) if weights else None

class WeightTracker:
    """Main system class managing weight records and statistics."""

    def __init__(self):
        # Using a list to store all weight records
        self._records = []

    def add_weight_record(self, date_str: str, weight_value: float) -> bool:
        """Add a new record if valid. Returns True on success."""
        try:
            record = WeightRecord(date_str, weight_value)
            self._records.append(record)
            return True
        except (ValueError, TypeError):
            # In this simulation context, we assume inputs are handled externally or validated strictly
            return False

    def get_stats(self) -> WeightStats:
        """Return the current statistics object."""
        if not self._records:
            raise ValueError("No weight records available to generate statistics.")
        
        stats = WeightStats(self._records.copy())
        # The copy ensures we don't modify original list order inside stats logic, 
        # though Order is preserved in lists. We just ensure independence for safety.
        return stats

    def display_statistics(self):
        """Prints the current statistics to stdout."""
        try:
            stats = self.get_stats()
            
            print("\n--- Weight Tracking Statistics ---")
            count = stats.calculate_total_count()
            avg_weight = stats.calculate_average()
            min_w = stats.get_min_weight()
            max_w = stats.get_max_weight()

            print(f"Total Records: {count}")
            if count > 0:
                print(f"Average Weight: {avg_weight} kg")
                print(f"Minimum Weight: {min_w} kg")
                print(f"Maximum Weight: {max_w} kg")
                
                # Optional breakdown by date for clarity in a small dataset
                sorted_records = self._records.copy()
                # Sort descending by weight to see the trend visually if needed, 
                # but keeping chronological order is usually better. Let's stick to simple stats.
            else:
                print("No data available.")

        except ValueError as e:
            print(f"Error generating statistics: {e}")

if __name__ == '__main__':
    # Initialize the tracker with hard-coded sample values 
    # representing a week of weight measurements.
    tracker = WeightTracker()

    # Simulate inputting new weights directly into the system state
    sample_entries = [
        ("2023-10-01", 75.5),
        ("2023-10-08", 76.2),
        ("2023-10-15", 74.8),
        ("2023-10-22", 75.9)
    ]

    # Process sample data without user prompts or file I/O
    for date, weight in sample_entries:
        tracker.add_weight_record(date, weight)

    # Display the updated statistics after adding samples
    tracker.display_statistics()