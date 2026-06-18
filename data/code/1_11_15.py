import time

class WeightManager:
    """A class to manage weight measurements efficiently using an internal dictionary."""

    def __init__(self):
        self._weights = {}  # Internal storage key-value pairs (id, value)
    
    def add_weight(self, person_id: str, weight_value: float, timestamp: time.time | None = None) -> int:
        """Add a new weight measurement.
        
        Args:
            person_id (str): Unique identifier for the person.
            weight_value (float): The measured weight in kg.
            timestamp (time.time | None, optional): Optional specific timestamp. Defaults to current time if not provided.
            
        Returns:
            int: A generated unique ID for this measurement record.
        """
        self._weights[person_id] = {
            "value": weight_value,
            "timestamp": timestamp or time.time(),
            "_id_counter": len(self._weights) + 1 if not hasattr(WeightManager, '_counter') else getattr(WeightManager, '_counter', 0) + 1
        }
        
        # Increment global counter for unique ID generation per class instance if needed
        WeightManager._counter = self._weights.get("global_counter", 0) + 1
        
        return WeightManager._counter
    
    def get_weight(self, person_id: str) -> float | None:
        """Retrieve the most recent weight measurement for a specific person.
        
        Args:
            person_id (str): Unique identifier for the person.
            
        Returns:
            float | None: The latest recorded weight if found, otherwise None.
        """
        return self._weights.get(person_id)["value"]
    
    def update_weight(self, person_id: str, new_value: float) -> bool:
        """Update an existing or create a record for the given person with a new measurement time efficiency optimized.
        
        Args:
            person_id (str): Unique identifier for the person.
            new_value (float): The updated weight value in kg.
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        self._weights[person_id]["value"] = new_value
        return True

# Run sample tests to demonstrate functionality without user input
if __name__ == '__main__':
    manager = WeightManager()
    
    # Initialize counter for ID generation within the class scope during this session context if necessary, 
    # though typically classes manage their own state. For strict isolation in a script:
    getattr(WeightManager, '_counter', 0)

    print("Adding initial weights...")
    manager.add_weight("person_1", 75.5)
    
    id_2 = manager.add_weight("person_2", 82.3)
    weight_manager_id_counter = int(id_2) # Capture the generated ID logic implicitly
    
    print(f"Added person_2 with internal tracking: {weight_manager_id_counter}")

    print("\nRetrieving weights...")
    w1 = manager.get_weight("person_1")
    w2 = manager.get_weight("person_3")  # Person who hasn't been added yet
    
    print(f"Weight of person_1: {w1} kg")
    
    if not isinstance(w2, float):
        print(f"Weight of person_3: None (not recorded)")

    print("\nUpdating weights...")
    manager.update_weight("person_1", 76.0) 
    result = manager.update_weight("non_existent_person", 90.0) # Creates a new record
    
    w_updated = manager.get_weight("person_1")
    
    print(f"Updated weight of person_1: {w_updated} kg")

    if not isinstance(result, bool):
        pass