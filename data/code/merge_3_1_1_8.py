import time

class WeightManager:
    """A class to manage weight measurements using a dictionary for efficient lookups."""
    
    def __init__(self):
        self._weights = {}  # Internal storage: {date_string: float}
        
    def add_weight(self, date_str, weight):
        """Add or update a weight measurement.
        
        Args:
            date_str (str): The date string in 'YYYY-MM-DD' format.
            weight (float): The recorded weight value.
            
        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            # Validate and parse date to ensure uniqueness based on day only if needed, 
            # but here we assume exact string match for simplicity as per task description.
            parsed_date = time.strptime(date_str, "%Y-%m-%d")
            self._weights[date_str] = weight
        except ValueError:
            raise ValueError(f"Invalid date format '{date_str}'. Expected 'YYYY-MM-DD'.")

    def get_weight(self, date_str):
        """Retrieve a specific weight measurement.
        
        Args:
            date_str (str): The date string in 'YYYY-MM-DD' format.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self._weights.get(date_str)

    def update_weight(self, date_str, new_weight):
        """Update an existing weight measurement.
        
        Args:
            date_str (str): The date string in 'YYYY-MM-DD' format.
            new_weight (float): The updated weight value.
            
        Raises:
            ValueError: If the record does not exist or if input validation fails.
        """
        try:
            parsed_date = time.strptime(date_str, "%Y-%m-%d")
            current_weight = self._weights.get(date_str)
            if current_weight is None:
                raise KeyError(f"No weight found for date '{date_str}'.")
            
            # Update the value; we could also choose to append history here.
            self._weights[date_str] = new_weight
            
        except ValueError as ve:
            raise ve

    def get_all_weights(self):
        """Return a copy of all stored weights sorted by date."""
        return dict(sorted(self._weights.items()))

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    
    manager = WeightManager()
    
    # Initial data entry
    manager.add_weight("2023-10-05", 70.5)
    manager.add_weight("2023-10-10", 69.8)
    manager.add_weight("2023-10-15", 70.2)
    
    # Update existing entry (simulating a correction or new measurement on same day logic if supported, 
    # though here we treat it as updating the specific key)
    manager.update_weight("2023-10-10", 69.5)
    
    # Retrieve specific weight
    retrieved = manager.get_weight("2023-10-10")
    print(f"Weight on 2023-10-10: {retrieved}")
    
    # Get all weights sorted by date
    all_weights = manager.get_all_weights()
    for date, weight in all_weights.items():
        print(f"{date}: {weight} kg")