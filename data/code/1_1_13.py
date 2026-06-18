class WeightManager:
    """A class to manage weight measurements using a dictionary for fast lookups."""

    def __init__(self):
        self._weights = {}  # Dictionary to store weights with date keys in format 'YYYY-MM-DD'

    def add_weight(self, person_name: str, weight: float) -> None:
        """Add or update the latest recorded weight for a specific person.
        
        Args:
            person_name (str): The name of the individual.
            weight (float): The new weight measurement in kilograms.
            
        Raises:
            ValueError: If the provided weight is not positive.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        
        # Update or create entry with today's date as key to ensure latest record is first
        self._weights[person_name] = weight

    def get_latest_weight(self, person_name: str) -> float | None:
        """Retrieve the most recent recorded weight for a specific person.
        
        Args:
            person_name (str): The name of the individual.
            
        Returns:
            float or None: The latest weight if found, otherwise None.
        """
        return self._weights.get(person_name)

    def get_all_weights(self) -> dict[str, float]:
        """Retrieve a copy of all stored weights.
        
        Returns:
            dict: A dictionary containing all person names and their corresponding weights.
        """
        # Return a shallow copy to prevent external modification affecting internal state
        return self._weights.copy()

    def remove_weight(self, person_name: str) -> bool:
        """Remove the weight record for a specific person if it exists.
        
        Args:
            person_name (str): The name of the individual whose record should be removed.
            
        Returns:
            bool: True if a record was successfully deleted, False otherwise.
        """
        return self._weights.pop(person_name, None) is not None

if __name__ == '__main__':
    # Hard-coded sample values for testing the WeightManager class
    
    manager = WeightManager()

    # Adding initial weights
    manager.add_weight("Alice", 65.0)
    manager.add_weight("Bob", 78.5)
    
    # Updating Alice's weight (simulating a new measurement later in time, though logic uses overwrite for simplicity 
    # as per standard 'latest' requirement without explicit date tracking in this simplified version)
    manager.add_weight("Alice", 64.2)

    print(f"Alice's latest weight: {manager.get_latest_weight('Alice')}")
    print(f"Bob's latest weight: {manager.get_latest_weight('Bob')}")
    
    all_data = manager.get_all_weights()
    print("\nAll records:")
    for person, w in all_data.items():
        print(f"{person}: {w} kg")

    # Removing Bob's record
    removed = manager.remove_weight("Bob")
    if removed:
        print(f"\nRemoved 'Bob'. Current count of people tracked: {len(manager.get_all_weights())}")
    
    # Attempting to retrieve non-existent person (should return None)
    result = manager.get_latest_weight("Charlie")
    print(f"Charlie's weight (not found): {result}")