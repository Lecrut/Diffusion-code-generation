import time

class WeightManager:
    """
    An optimized class to manage weight measurements using a dictionary internally.
    
    Attributes:
        data (dict): Internal storage for weights where keys represent identifiers 
                     and values represent the recorded weight as floats.
"""

    def __init__(self, initial_data=None):
        """Initialize the WeightManager with optional pre-loaded data."""
        self.data = {}
        if isinstance(initial_data, dict):
            # Ensure all new entries are stored correctly even if input has non-float values
            for key in initial_data:
                value = float(initial_data[key])
                self._store(key, value)

    def _validate_key(self, key):
        """Ensure the identifier is hashable."""
        try:
            hash(key)
        except TypeError:
            raise ValueError("Weight identifiers must be hashable (e.g., strings or numbers).")

    def store(self, weight_id, value):
        """
        Store a new weight measurement.
        
        Args:
            weight_id (hashable): Unique identifier for the entry.
            value (float): The numerical weight to record.
            
        Raises:
            ValueError: If 'value' cannot be converted to float or if 'weight_id' is invalid.
        """
        try:
            self._validate_key(weight_id)
            stored_value = float(value)
            # Using direct assignment ensures O(1) average time complexity for insertion
            self.data[weight_id] = stored_value
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input for weight ID '{weight_id}' or value {value}.")

    def retrieve(self, weight_id):
        """
        Retrieve a specific weight measurement.
        
        Args:
            weight_id (hashable): Unique identifier to look up.
            
        Returns:
            float: The stored weight if found, otherwise None.
            
        Raises:
            ValueError: If 'weight_id' is invalid.
        """
        try:
            self._validate_key(weight_id)
            return self.data.get(weight_id)
        except (ValueError, TypeError):
            raise

    def update(self, weight_id, new_value):
        """
        Update an existing weight measurement or store a new one if it doesn't exist.
        
        Args:
            weight_id (hashable): Unique identifier of the entry to update.
            new_value (float): The updated numerical value for the weight.
            
        Raises:
            ValueError: If 'weight_id' is invalid, existing key not found on update-only mode 
                       (if implemented strictly), or if conversion fails.
                       
        Note: This implementation treats this as a "store" operation to ensure robustness,
              effectively replacing any old value with the new one for efficiency and simplicity.
        """
        try:
            self._validate_key(weight_id)
            stored_value = float(new_value)
            # Direct assignment replaces existing key in O(1) time complexity
            self.data[weight_id] = stored_value
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input for weight ID '{weight_id}' or value {new_value}.")

    def get_all(self):
        """Return a copy of all stored measurements to prevent external modification."""
        return dict(self.data)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input, CLI args, or network access used.
    
    # Initialize with some pre-existing data for demonstration
    initial_weights = {
        "user_001": 75.5,
        "user_002": 82.3,
        "user_003": 90.1
    }

    manager = WeightManager(initial_data=initial_weights)

    # Test Store operation
    print("--- Testing Store ---")
    try:
        manager.store("new_user", 65.4)
        print(f"Stored 'new_user': {manager.retrieve('new_user')}")
        
        # Attempt invalid value type (should raise error if strictly enforced, 
        # but float() handles string conversion usually; let's test with bad input logic implicitly via try-except in store)
    except ValueError as e:
        print(f"Error during store: {e}")

    # Test Update operation
    print("\n--- Testing Update ---")
    manager.update("user_001", 76.2)
    current_val = manager.retrieve("user_001")
    print(f"Updated 'user_001' to: {current_val}")

    # Test Retrieve non-existent key (returns None as per implementation logic using .get())
    print("\n--- Testing Retrieve Non-Existent ---")
    result = manager.retrieve("non_existent_user")
    if result is None:
        print(f"Key 'non_existent_user' not found. Result: {result}")

    # Test Get All operations
    print("\n--- Testing Get All ---")
    all_weights = manager.get_all()
    for key, value in sorted(all_weights.items()):
        print(f"{key}: {value} kg")

    # Performance check simulation (optional internal logic)
    start_time = time.time()
    
    # Simulate bulk storage to ensure efficiency isn't impacted by loops
    performance_data = [f"perf_user_{i}" for i in range(100)]
    perf_values = [float(i * 2.5 + 40.0) for i in range(100)]

    for idx, key in enumerate(performance_data):
        manager.store(key, perf_values[idx])

    end_time = time.time()
    
    print(f"\n--- Performance Test ---")
    print(f"Stored 100 items. Total execution time: {end_time - start_time:.6f} seconds.")
    
    # Verify one of the performance entries
    if len(manager.data) == 132: 
        print("All operations completed successfully with expected data count (Initial + New).")
    else:
        print(f"Unexpected data count. Expected 132, got {len(manager.data)}.")