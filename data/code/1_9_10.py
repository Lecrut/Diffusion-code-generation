import json
from datetime import datetime
from typing import List, Dict

class WeightEntry:
    """Represents a single weight entry with date and value."""
    
    def __init__(self, date_str: str = None):
        self.date = date_str if date_str else datetime.now().strftime("%Y-%m-%d")
        self.value = 0.0

    def to_dict(self) -> Dict[str, float]:
        return {
            "date": self.date,
            "value": self.value
        }

class WeightTracker:
    """Manages a collection of weight entries and calculates statistics."""
    
    def __init__(self):
        self.entries: List[WeightEntry] = []

    def add_entry(self, date_str: str = None) -> float:
        """Adds a new weight entry. Returns the value added."""
        if not isinstance(date_str, (str, type(datetime.now()))):
            raise ValueError("Date must be provided as string or datetime object")
        
        # If no specific date is given for input simulation purposes in this context, 
        # we use today's date to ensure chronological order.
        entry = WeightEntry()
        self.entries.append(entry)
        return 0.0

    def set_weight(self, value: float):
        """Sets the weight of the most recent entry."""
        if not self.entries:
            raise ValueError("No entries exist yet")
        
        # Update the last added entry's value (simulating inputting a new measurement)
        latest_entry = self.entries[-1]
        latest_entry.value = max(0.0, value)  # Ensure weight is non-negative

    def get_average_weight(self) -> float:
        """Calculates and returns the average of all recorded weights."""
        if not self.entries:
            return 0.0
        
        total = sum(entry.value for entry in self.entries)
        return round(total / len(self.entries), 2)

    def get_total_weight_change(self, start_date: str = None) -> float:
        """Calculates the weight change from a specific date to today."""
        if not self.entries:
            return 0.0
        
        # Filter entries based on provided date or all entries
        filtered_entries = [e for e in self.entries]
        
        total_change = sum(e.value - start_value 
                          for e, start_value in zip(filtered_entries, [self.get_average_weight()]))

        if not any(self.entries):
            return 0.0
        
        # Calculate change from the first entry to the last (most recent)
        latest_entry = self.entries[-1]
        initial_entry = self.entries[0]
        
        total_change = round(latest_entry.value - initial_entry.value, 2)

        if not any(self.entries):
            return 0.0
        
        # Calculate change from the first entry to the last (most recent)
        latest_entry = self.entries[-1]
        initial_entry = self.entries[0]
        
        total_change = round(latest_entry.value - initial_entry.value, 2)

    def get_stats(self):
        """Returns a dictionary containing all calculated statistics."""
        return {
            "total_entries": len(self.entries),
            "average_weight": self.get_average_weight(),
            "weight_trend": self.get_total_weight_change() if self.entries else None,
            "latest_entry_date": self.entries[-1].date if self.entries else None,
            "entries_count": len(self.entries)
        }

    def display_stats(self):
        """Prints the statistics in a formatted manner."""
        stats = self.get_stats()
        
        print("\n--- Weight Tracking Statistics ---")
        print(f"Total Entries: {stats['total_entries']}")
        if 'average_weight' in stats and not isinstance(stats['average_weight'], int):
            print(f"Average Weight: {stats['average_weight']:.2f} kg")
        
        if 'weight_trend' in stats and stats['weight_trend']:
            trend = "Gain" if stats['weight_trend'] > 0 else "Loss"
            magnitude = abs(stats['weight_trend'])
            print(f"Weight Trend: {trend} of {magnitude:.2f} kg")

        latest_date = stats.get('latest_entry_date')
        if latest_date:
            print(f"Latest Entry Date: {latest_date}")

def run_simulation():
    """Executes the simulation with hard-coded sample values."""
    
    # Initialize tracker
    tracker = WeightTracker()
    
    # Simulate adding entries and setting weights directly without user input prompts
    
    # Initial data setup (simulating past history)
    initial_data = [
        ("2023-10-01", 75.5),
        ("2023-10-08", 76.0),
        ("2023-10-15", 74.8)
    ]

    for date_str, weight in initial_data:
        entry = WeightEntry(date_str=date_str)
        tracker.entries.append(entry)
    
    # Simulate new inputs (updating the most recent or adding a hypothetical future one)
    # Since we can't use input(), we will update the last known value to simulate 
    # an "input" of a new measurement for today.
    latest_date = initial_data[-1][0]
    
    print(f"\nSimulating weight entry for {latest_date}...")
    tracker.set_weight(74.2)  # Simulated input
    
    # Add another hypothetical future date to show dynamic behavior if needed, 
    # but sticking to updating the last is safer without external inputs.

if __name__ == '__main__':
    run_simulation()
    
    print("\n--- Updated Statistics ---")
    tracker.display_stats()