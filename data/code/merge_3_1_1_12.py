class WeightManager:
    """A class to manage weight measurements with fast dictionary-based lookups."""
    
    def __init__(self):
        # Internal storage using a dictionary where keys represent individuals and values their weights
        self.weight_data = {}
    
    def add_weight(self, person_id, new_weight):
        """Adds or updates the weight of an individual.
        
        Args:
            person_id (str | int): Unique identifier for the individual.
            new_weight (float): The new weight value to record.
        """
        if not isinstance(new_weight, (int, float)):
            raise ValueError("Weight must be a numeric type.")
        self.weight_data[person_id] = round(new_weight, 2)

    def get_current_weight(self, person_id):
        """Retrieves the current weight of an individual.
        
        Args:
            person_id (str | int): Unique identifier for the individual.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self.weight_data.get(person_id)

    def remove_weight(self, person_id):
        """Removes a specific individual's weight record from storage.
        
        Args:
            person_id (str | int): Unique identifier for the individual to delete.
            
        Raises:
            KeyError: If the ID does not exist in the records.
        """
        del self.weight_data[person_id]

    def get_average_weight(self, list_of_ids):
        """Calculates and returns the average weight of a group of individuals.
        
        Args:
            list_of_ids (list[str | int]): List of unique identifiers to include in calculation.
            
        Returns:
            float or None: The calculated average weight if at least one ID exists, else None.
        """
        weights = [self.weight_data.get(pid) for pid in list_of_ids]
        
        # Filter out any missing entries (None), though ideally these IDs should exist first
        valid_weights = [w for w in weights if w is not None]

        if len(valid_weights) == 0:
            return None
        
        return sum(valid_weights) / len(valid_weights)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    
    wm = WeightManager()
    
    # Adding initial measurements
    wm.add_weight("Alice", 145.67)
    wm.add_weight("Bob", 82.30)
    wm.add_weight("Charlie", 90.50)

    print(f"Current weight of Alice: {wm.get_current_weight('Alice')} kg") # Output: Current weight of Alice: 145.67 kg
    
    # Update Charlie's measurement later (simulating a subsequent action before retrieval)
    wm.add_weight("Charlie", 91.20) 

    print(f"Updated current weight of Charlie: {wm.get_current_weight('Charlie')} kg") 
    
    # Get the average for everyone present in the sample block initially and after updates
    avg = wm.get_average_weight(["Alice", "Bob"]) 
    print(f"Average weight of Alice & Bob: {avg} kg") 

    # Attempting to remove a non-existent ID should raise KeyError as per logic if accessed directly,
    # but using get() avoids exception. To demonstrate removal with valid key usage in the context of the class design:

    try:
        wm.remove_weight("Charlie") 
        print(f"Weight removed for Charlie.")
        
        # Try to retrieve after deletion (should return None)
        final_charlie = wm.get_current_weight("Charlie")
        if final_charlie is None:
            print("Confirmed: No record found for Charlie anymore.")
    except Exception as e:
        print(f"Error during removal logic check due to exception handling specifics in context: {e}")

    # Demonstrate average calculation with only remaining members (since Charlie was removed)
    avg_remaining = wm.get_average_weight(["Alice", "Bob"]) 
    print(f"Average weight of Alice & Bob after removing Charlie: {avg_remaining} kg")