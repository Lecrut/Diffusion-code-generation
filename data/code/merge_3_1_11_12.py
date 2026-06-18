class WeightManager:
    """
    A class to manage weight measurements efficiently using a dictionary.
    
    Attributes:
        data (dict): Internal storage for weights, where keys are unique identifiers 
                     and values are the recorded weights.
        
    Methods:
        add_weight(identifier, measurement): Adds or updates a weight record.
        get_weight(identifier): Retrieves a specific weight by identifier.
        remove_weight(identifier): Removes a weight record by identifier.
        list_weights(): Returns all current measurements as a dictionary copy.
    
    Time Complexity: O(1) for add, get, and remove operations on average due to hash map usage.
    """

    def __init__(self):
        self.data = {}

    def add_weight(self, identifier: str, measurement: float) -> None:
        """
        Adds a new weight record or updates an existing one if the identifier exists.
        
        Args:
            identifier (str): Unique key for the weight entry.
            measurement (float): The numerical value of the weight.
            
        Raises:
            TypeError: If 'identifier' is not a string or 'measurement' is not numeric.
        """
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be a string.")
        if not isinstance(measurement, (int, float)):
            raise TypeError("Measurement must be an integer or float.")

        self.data[identifier] = measurement

    def get_weight(self, identifier: str) -> float | None:
        """
        Retrieves the weight associated with the given identifier.
        
        Args:
            identifier (str): The key to look up in the dictionary.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
            
        Raises:
            TypeError: If 'identifier' is not a string.
        """
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be a string.")

        return self.data.get(identifier)

    def remove_weight(self, identifier: str) -> bool:
        """
        Removes the weight record associated with the given identifier.
        
        Args:
            identifier (str): The key to delete from the dictionary.
            
        Returns:
            bool: True if a record was removed and it existed; False otherwise.
            
        Raises:
            TypeError: If 'identifier' is not a string.
        """
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be a string.")

        return self.data.pop(identifier, None) is not None

    def list_weights(self) -> dict[str, float]:
        """
        Returns a copy of all current weight measurements.
        
        Returns:
            dict[str, float]: A shallow copy of the internal data dictionary.
        """
        return self.data.copy()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = WeightManager()

    # Add initial measurements
    manager.add_weight("user_001", 75.5)
    manager.add_weight("user_002", 82.3)
    
    # Update an existing measurement (simulating a new reading for user_001)
    manager.add_weight("user_001", 76.2)

    print("--- Weight Manager Operations ---")
    
    # Retrieve specific weight
    retrieved = manager.get_weight("user_001")
    print(f"Weight of 'user_001': {retrieved}")

    # List all weights
    all_weights = manager.list_weights()
    print("\nAll recorded weights:")
    for user, weight in all_weights.items():
        print(f"- {user}: {weight} kg")

    # Remove a specific entry to test removal logic (though we keep it visible above)
    # Let's remove 'user_002' instead of the updated one to show deletion capability clearly
    removed = manager.remove_weight("user_002")
    print(f"\nRemoved user_002: {removed}")

    final_list = manager.list_weights()
    print("\nFinal state:")
    for user, weight in final_list.items():
        print(f"- {user}: {weight} kg")