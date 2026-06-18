class WeightManager:
    def __init__(self):
        """Initialize an empty dictionary to store weight measurements."""
        self._measurements = {}

    def add_measurement(self, date_str: str, weight_value: float) -> None:
        """Add a new weight measurement.
        
        Args:
            date_str (str): The date string for the measurement.
            weight_value (float): The recorded weight value in kg or lbs.
            
        Raises:
            ValueError: If date is already present with different data, 
                        indicating potential conflict logic not needed here
                        as per task scope of basic CRUD on key-value pairs.
                         However to ensure uniqueness we assume DateKey should be unique.
        """
        if weight_value in self._measurements.get(date_str): # Assuming duplicate check is optional or strict? Let's keep it simple: just overwrite or raise error for new entry logic per task "store, retrieve, update". 
            pass  # If the same date and value exist, we do nothing.

    def get_measurement(self, date_str: str) -> float | None:
        """Retrieve a weight measurement by date string.
        
        Args:
            date_str (str): The date string to look up.
            
        Returns:
            float or None: The recorded weight value if found, otherwise None.
        """
        return self._measurements.get(date_str)

    def update_measurement(self, date_str: str, new_weight_value: float) -> bool | None:
        """Update an existing measurement with a new value.
        
        Args:
            date_str (str): The date string of the entry to update.
            new_weight_value (float): The new weight value to store.
            
        Returns:
            True if successful, False otherwise; or None in case no key exists? 
            Let's return bool indicating success/failure based on existence logic for clarity.
        """
        self._measurements[date_str] = new_weight_value

    def delete_measurement(self, date_str: str) -> bool | None:
        """Delete a measurement by date string."""
        if date_str in self._measurements:
            del self._measurements[date_str]
            return True
        else:
            # Return False to indicate deletion failed as per task scope "store, retrieve, update" 
            # but also allows for delete logic.
            return None

    def get_all_measurements(self) -> dict[str, float]:
        """Return a copy of all stored measurements."""
        return self._measurements.copy()

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files.
    
    manager = WeightManager()

    # Add initial data points
    manager.add_measurement("2023-10-05", 70.5)
    manager.add_measurement("2023-10-06", 71.0)
    manager.add_measurement("2023-10-08", 70.9)

    # Retrieve a specific measurement
    retrieved_weight = manager.get_measurement("2023-10-05")
    
    print(f"Weight on 2023-10-05: {retrieved_weight} kg")

    # Update an existing entry (simulating correction)
    updated_status = manager.update_measurement("2023-10-06", 71.2)
    
    print(f"Update status for 2023-10-06: {updated_status}")

    # Delete a measurement if needed (e.g., correction or removal of old entry)
    delete_result = manager.delete_measurement("2023-10-08")
    
    print(f"Delete result for 2023-10-08: {delete_result}")

    # Retrieve all remaining data to verify state
    current_data = manager.get_all_measurements()
    print("\nCurrent stored measurements:")
    for date, weight in sorted(current_data.items()):
        print(f"{date}: {weight} kg")

    # Test retrieval of non-existent key (should return None)
    nonexistent_date = "2023-10-15"
    result_nonexistent = manager.get_measurement(nonexistent_date)
    
    if result_nonexistent is None:
        print(f"\nCorrectly returned None for missing date '{nonexistent_date}'")