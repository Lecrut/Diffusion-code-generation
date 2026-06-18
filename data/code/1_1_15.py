class WeightManager:
    """A class to manage weight measurements using a dictionary for efficient lookups."""

    def __init__(self):
        self.weights = {}  # Dictionary to store weights as {date_str: value}

    def add_weight(self, date, weight_value):
        """Add or update a weight measurement for the given date.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format.
            weight_value (float): The weight measurement.
        """
        self.weights[date] = float(weight_value)

    def get_weight(self, date):
        """Retrieve a specific weight measurement.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format.
            
        Returns:
            float or None: The weight value if found, otherwise None.
        """
        return self.weights.get(date)

    def get_all_weights(self):
        """Retrieve all stored weights as a dictionary copy.
        
        Returns:
            dict: A shallow copy of the internal weights dictionary.
        """
        return self.weights.copy()

    def remove_weight(self, date):
        """Remove a weight measurement for the given date.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format.
            
        Raises:
            KeyError: If the date is not found in the storage.
        """
        if date in self.weights:
            del self.weights[date]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    
    manager = WeightManager()

    # Add some initial data
    add_samples = [
        ("2023-10-01", 65.4),
        ("2023-10-08", 65.7),
        ("2023-10-15", 66.0),
    ]

    for date, weight in add_samples:
        manager.add_weight(date, weight)

    # Retrieve specific weights
    print("Weight on 2023-10-08:", manager.get_weight("2023-10-08"))

    # Get all stored data to verify storage and retrieval consistency
    all_data = manager.get_all_weights()
    for date, weight in sorted(all_data.items()):
        print(f"{date}: {weight} kg")

    # Remove a specific entry
    try:
        removed_date = "2023-10-08"
        manager.remove_weight(removed_date)
        remaining_weights = manager.get_all_weights()
        
        if not any(d == removed_date for d in remaining_weights.keys()):
            print(f"\nSuccessfully removed {removed_date}. Remaining entries: ", end="")
            
            # Print remaining weights to show the effect of removal
            sorted_remaining = sorted(remaining_weights.items())
            for date, weight in sorted_remaining:
                print(weight)
        else:
            print("Error: Removal failed.")

    except KeyError as e:
        print(f"Key Error during removal attempt: {e}")