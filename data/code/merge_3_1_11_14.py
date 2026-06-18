class WeightManager:
    """A class to manage weight measurements with efficient storage and retrieval."""
    
    def __init__(self):
        # Internal dictionary to store weights, keys should be unique identifiers (e.g., date or ID)
        self._weights = {}

    def add_weight(self, identifier, value):
        """Add a new weight measurement.
        
        Args:
            identifier (str | int): Unique key for the entry (e.g., '2023-10-01' or 'user_456').
            value (float): The weight value to record, must be numeric.
            
        Raises:
            TypeError: If identifier is not hashable or value is not a number.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Weight value must be an integer or float.")
        
        self._weights[identifier] = round(value, 2)

    def get_weight(self, identifier):
        """Retrieve the weight measurement for a specific identifier.
        
        Args:
            identifier (str | int): Unique key for the entry.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self._weights.get(identifier)

    def update_weight(self, identifier, new_value):
        """Update an existing weight measurement.
        
        Args:
            identifier (str | int): Unique key for the entry to be updated.
            new_value (float): The new weight value to set.
            
        Raises:
            KeyError: If the identifier does not exist in the manager.
            TypeError: If new_value is not a number.
        """
        if identifier not in self._weights:
            raise KeyError(f"No record found for identifier '{identifier}'.")
        
        if not isinstance(new_value, (int, float)):
            raise TypeError("New weight value must be an integer or float.")
            
        # Update the existing entry with rounded precision to avoid floating point drift accumulation
        self._weights[identifier] = round(new_value, 2)

    def remove_weight(self, identifier):
        """Remove a weight measurement.
        
        Args:
            identifier (str | int): Unique key for the entry to be removed.
            
        Raises:
            KeyError: If the identifier does not exist in the manager.
        """
        if identifier not in self._weights:
            raise KeyError(f"No record found for identifier '{identifier}'.")
        
        del self._weights[identifier]

    def get_all_weights(self):
        """Retrieve all stored weight measurements as a dictionary copy to prevent external modification affecting internal state.
        
        Returns:
            dict: A shallow copy of the internal weights dictionary.
        """
        return self._weights.copy()

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    manager = WeightManager()

    # Adding initial entries
    manager.add_weight("2023-10-05", 70.5)
    manager.add_weight("2023-10-12", 68.9)
    manager.add_weight(1, 72.0)

    # Retrieving specific weights
    print(f"Weight on 2023-10-12: {manager.get_weight('2023-10-12')}")
    weight_user_1 = manager.get_weight(1)
    
    if weight_user_1 is None:
        # Fallback for display logic since key was int in add but checked as string implicitly here? 
        # Correction: In Python `if` checks object identity. The code above used integer 1 correctly in add, so it should return float.
        print(f"Weight user 1 (int): {weight_user_1}")

    # Updating an existing entry
    try:
        manager.update_weight("2023-10-12", 69.5)
        updated_val = manager.get_weight("2023-10-12")
        print(f"Updated weight on 2023-10-12 to: {updated_val}")
    except KeyError as e:
        # This shouldn't happen with valid sample data, but handles robustness if ID changed
        pass

    # Attempting update on non-existent key to demonstrate error handling (optional for silent failure)
    try:
        manager.update_weight("nonexistent", 75.0)
    except KeyError as e:
        print(f"Expected Error caught: {e}")

    # Removing an entry
    manager.remove_weight(1)
    
    # Verifying removal by trying to access the removed key (which should fail silently in get or raise error here if we tried update)
    try:
        _ = manager.get_weight(1) # Should return None now due to remove logic? No, remove uses del. Let's check existence via a dummy operation logic simulation
    
    except KeyError as e:
        print(f"Expected Error after removal caught (if accessed for write): {e}")

    final_status = "Success - All operations executed without external dependencies."