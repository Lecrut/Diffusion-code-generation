class WeightManager:
    """A class to manage weight measurements using a dictionary for efficient lookups."""

    def __init__(self):
        self._weights = {}  # Dictionary to store weights with date strings as keys

    def add_weight(self, person_name, weight_value):
        """Adds or updates the weight of a specific person.
        
        Args:
            person_name (str): The name of the person.
            weight_value (float): The weight measurement in kilograms.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self._weights[person_name] = float(weight_value)
            return True
        except ValueError:
            print(f"Error: Invalid weight value '{weight_value}' for person '{person_name}'.")
            return False

    def get_weight(self, person_name):
        """Retrieves the current weight of a specific person.
        
        Args:
            person_name (str): The name of the person whose weight is needed.
            
        Returns:
            float or None: The weight in kilograms if found, otherwise None.
        """
        return self._weights.get(person_name)

    def update_weight(self, person_name, new_weight_value):
        """Updates the existing weight record for a specific person.
        
        Args:
            person_name (str): The name of the person whose weight is being updated.
            new_weight_value (float): The new weight measurement in kilograms.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self._weights[person_name] = float(new_weight_value)
            return True
        except ValueError:
            print(f"Error: Invalid new weight value '{new_weight_value}' for person '{person_name}'.")
            return False

    def remove_weight(self, person_name):
        """Removes the weight record of a specific person.
        
        Args:
            person_name (str): The name of the person whose record is to be removed.
            
        Returns:
            bool: True if successful and key existed, False otherwise.
        """
        return self._weights.pop(person_name, None) is not None

    def get_all_weights(self):
        """Returns a dictionary containing all stored weight measurements.
        
        Returns:
            dict: A copy of the internal weights dictionary to prevent external modification.
        """
        return self._weights.copy()

if __name__ == '__main__':
    # Hard-coded sample values for testing
    
    manager = WeightManager()

    # Adding initial data
    print("Adding weights...")
    success1 = manager.add_weight("Alice", 65.5)
    success2 = manager.add_weight("Bob", 70.2)
    success3 = manager.add_weight("Charlie", 82.9)

    # Retrieving data
    print("\nRetrieving weights...")
    alice_weight = manager.get_weight("Alice")
    bob_weight = manager.get_weight("Bob")
    
    if alice_weight is not None:
        print(f"Alice's weight: {alice_weight} kg")
    else:
        print("Alice's record not found.")

    # Updating data
    print("\nUpdating weights...")
    update_success = manager.update_weight("Alice", 67.0)
    
    if update_success and alice_weight is None or (manager.get_weight("Alice") == 67.0):
        new_alice_weight = manager.get_weight("Alice")
        print(f"Alice's updated weight: {new_alice_weight} kg")

    # Removing data
    print("\nRemoving weights...")
    remove_success = manager.remove_weight("Bob")
    
    if not remove_success or (manager.get_weight("Bob") is None):
        print("Bob's record removed successfully.")

    # Displaying all records
    print("\nAll current weight records:")
    for person, value in manager.get_all_weights().items():
        print(f"{person}: {value} kg")