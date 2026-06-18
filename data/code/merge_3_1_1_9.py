class WeightManager:
    """A class to manage weight measurements using a dictionary for efficient lookups."""

    def __init__(self):
        self._weights = {}  # Dictionary to store weights with date strings as keys

    def add_measurement(self, person_name, weight_kg):
        """Adds or updates a weight measurement for a specific person.
        
        Args:
            person_name (str): The name of the person.
            weight_kg (float): The weight in kilograms.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self._weights[person_name] = weight_kg
            return True
        except Exception as e:
            print(f"Error adding measurement for {person_name}: {e}")
            return False

    def get_measurement(self, person_name):
        """Retrieves the latest weight measurement for a specific person.
        
        Args:
            person_name (str): The name of the person whose weight is needed.
            
        Returns:
            float or None: The weight in kilograms if found, otherwise None.
        """
        return self._weights.get(person_name)

    def update_measurement(self, person_name, new_weight_kg):
        """Updates an existing weight measurement for a specific person.
        
        Args:
            person_name (str): The name of the person whose weight is being updated.
            new_weight_kg (float): The new weight in kilograms.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        return self.add_measurement(person_name, new_weight_kg)

    def remove_measurement(self, person_name):
        """Removes a weight measurement for a specific person.
        
        Args:
            person_name (str): The name of the person whose record is to be deleted.
            
        Returns:
            bool: True if successfully removed, False otherwise.
        """
        return self._weights.pop(person_name, None) is not None

    def get_all_measurements(self):
        """Returns a list containing all stored measurements as (name, weight) tuples."""
        return [(person, weight) for person, weight in self._weights.items()]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    
    manager = WeightManager()

    # Adding initial measurements
    success1 = manager.add_measurement("Alice", 65.0)
    success2 = manager.add_measurement("Bob", 78.5)
    
    print(f"Added Alice: {success1}")
    print(f"Added Bob: {success2}")

    # Retrieving measurements
    alice_weight = manager.get_measurement("Alice")
    bob_weight = manager.get_measurement("Bob")
    unknown_weight = manager.get_measurement("Charlie")

    print(f"Alice's weight: {alice_weight} kg")
    print(f"Bob's weight: {bob_weight} kg")
    print(f"Charlie's weight (should be None): {unknown_weight}")

    # Updating a measurement
    updated_success = manager.update_measurement("Alice", 67.5)
    new_alice_weight = manager.get_measurement("Alice")
    
    print(f"\nUpdated Alice to: {new_alice_weight} kg ({updated_success})")

    # Removing a measurement
    removed_success = manager.remove_measurement("Bob")
    bob_removed_check = manager.get_measurement("Bob")
    
    print(f"Removed Bob: {removed_success}")
    print(f"Bob's weight after removal (should be None): {bob_removed_check}")

    # Displaying all remaining measurements
    all_data = manager.get_all_measurements()
    if all_data:
        print("\nAll current records:")
        for name, w in all_data:
            print(f"{name}: {w} kg")
    else:
        print("\nNo records remain.")

    # Verify internal state integrity (optional debug output)
    print(f"\nInternal dictionary size: {len(manager._weights)}")