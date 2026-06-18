class WeightManager:
    """A class to manage weight measurements using a dictionary for fast lookups."""

    def __init__(self):
        self._weights = {}

    def add_measurement(self, date_str: str, weight_value: float) -> None:
        """Add or update a weight measurement.
        
        Args:
            date_str (str): The date string for the measurement (e.g., 'YYYY-MM-DD').
            weight_value (float): The recorded weight value in kilograms.
            
        Raises:
            ValueError: If date_str is empty and not provided, or if weight_value is invalid.
        """
        if not isinstance(date_str, str) or date_str.strip() == "":
            raise ValueError("Date string cannot be empty.")
        
        try:
            float(weight_value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid weight value: {weight_value}")

        self._weights[date_str] = round(float(weight_value), 2)

    def get_measurement(self, date_str: str) -> float | None:
        """Retrieve a specific weight measurement.
        
        Args:
            date_str (str): The date string for the desired measurement.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self._weights.get(date_str)

    def get_all_measurements(self) -> dict[str, float]:
        """Retrieve all stored measurements.
        
        Returns:
            dict[str, float]: A copy of the internal dictionary containing all dates and weights.
        """
        return {k: v for k, v in self._weights.items()}

    def update_measurement(self, date_str: str, new_weight_value: float) -> bool:
        """Update an existing weight measurement or raise an error if not found.
        
        Args:
            date_str (str): The date string of the measurement to update.
            new_weight_value (float): The new weight value in kilograms.
            
        Returns:
            bool: True if successfully updated, False otherwise.
        """
        try:
            self.add_measurement(date_str, new_weight_value)
            return True
        except ValueError as e:
            print(f"Error updating measurement for {date_str}: {e}")
            return False

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = WeightManager()

    # Adding initial measurements
    manager.add_measurement("2023-10-01", 75.5)
    manager.add_measurement("2023-10-08", 76.0)
    manager.add_measurement("2023-10-15", 74.8)

    # Retrieving specific measurement
    print(f"Weight on 2023-10-15: {manager.get_measurement('2023-10-15')} kg")

    # Updating a measurement (simulating adding again to update logic)
    manager.add_measurement("2023-10-15", 74.9) 
    print(f"Updated Weight on 2023-10-15: {manager.get_measurement('2023-10-15')} kg")

    # Retrieving all measurements
    all_data = manager.get_all_measurements()
    sorted_dates = sorted(all_data.keys())
    
    print("\nAll recorded weights:")
    for date in sorted_dates:
        print(f"{date}: {all_data[date]} kg")