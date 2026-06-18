import json

class WeightManager:
    """A class to manage weight measurements with fast dictionary lookups."""

    def __init__(self):
        self._weights = {}  # Dictionary to store weight data {date_str: value}

    def add_weight(self, date: str, weight: float) -> bool:
        """Add or update a weight measurement for the given date.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format.
            weight (float): The recorded weight value.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Basic validation for float conversion to handle invalid inputs gracefully
            val = float(weight)
            self._weights[date] = val
            return True
        except (ValueError, TypeError):
            return False

    def get_weight(self, date: str) -> float | None:
        """Retrieve the weight measurement for a specific date.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self._weights.get(date)

    def update_weight(self, date: str, new_value: float | int) -> bool:
        """Update the existing weight measurement for a given date.
        
        Args:
            date (str): The current date string in 'YYYY-MM-DD' format.
            new_value (float or int): The updated weight value.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            val = float(new_value)
            self._weights[date] = val
            return True
        except (ValueError, TypeError):
            return False

    def get_all_weights(self) -> dict[str, float]:
        """Retrieve all stored weight measurements.
        
        Returns:
            dict[str, float]: A copy of the internal weights dictionary.
        """
        # Return a deep copy to prevent external modification affecting internal state
        return self._weights.copy()

    def remove_weight(self, date: str) -> bool:
        """Remove a weight measurement for a specific date if it exists.
        
        Args:
            date (str): The current date string in 'YYYY-MM-DD' format.
            
        Returns:
            bool: True if removed or did not exist, False otherwise.
        """
        return self._weights.pop(date, None) is not None

    def get_stats(self) -> dict[str, float]:
        """Calculate basic statistics for all recorded weights.
        
        Returns:
            dict[str, float]: Dictionary containing 'count', 'min', 'max', and 'average'.
        """
        values = list(self._weights.values())
        if not values:
            return {
                "count": 0,
                "min": None,
                "max": None,
                "average": None
            }
        
        count = len(values)
        min_val = min(values)
        max_val = max(values)
        avg_val = sum(values) / count
        
        return {
            "count": count,
            "min": min_val,
            "max": max_val,
            "average": round(avg_val, 2)
        }

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files.
    
    manager = WeightManager()

    # Sample data: dates and weights in kg
    sample_data = [
        ("2023-10-01", 75.5),
        ("2023-10-08", 76.0),
        ("2023-10-15", 74.8),
        ("2023-10-22", 75.2)
    ]

    # Add sample weights
    for date, weight in sample_data:
        manager.add_weight(date, weight)

    print("Initial Storage:")
    all_weights = manager.get_all_weights()
    for d, w in sorted(all_weights.items()):
        print(f"  {d}: {w} kg")

    # Test retrieval and update
    target_date = "2023-10-15"
    retrieved_weight = manager.get_weight(target_date)
    print(f"\nRetrieved weight for {target_date}: {retrieved_weight}")

    updated_value = 74.9
    is_updated = manager.update_weight(target_date, updated_value)
    
    if is_updated:
        new_retrieval = manager.get_weight(target_date)
        print(f"Updated weight to {updated_value}, verified as {new_retrieval}")

    # Test stats calculation
    stats = manager.get_stats()
    print("\nStatistics:")
    print(f"  Count: {stats['count']}")
    if stats['min'] is not None:
        print(f"  Min: {stats['min']} kg")
    if stats['max'] is not None:
        print(f"  Max: {stats['max']} kg")
    if stats['average'] is not None:
        print(f"  Average: {stats['average']} kg")

    # Test removal and edge case handling with invalid input attempt (simulated logic)
    removed = manager.remove_weight("2023-10-15")
    print(f"\nRemoved weight for {target_date}: {removed}")
    
    final_stats = manager.get_stats()
    print("\nFinal Statistics after removal:")
    print(f"  Count: {final_stats['count']}")