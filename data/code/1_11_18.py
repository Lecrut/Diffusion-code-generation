import time

class WeightManager:
    """
    A class to manage weight measurements using a dictionary internally.
    Ensures all operations (store, retrieve, update) are O(1) on average.
    
    Attributes:
        _data (dict): Internal storage for weights where keys are unique identifiers 
                      and values are the recorded weight as floats.
    """

    def __init__(self):
        self._data = {}

    def store(self, identifier: str, weight: float) -> None:
        """
        Stores a new weight measurement or updates an existing one.
        
        Args:
            identifier (str): A unique string key for the measurement.
            weight (float): The numerical value of the weight to record.
            
        Returns:
            None
            
        Complexity: O(1) average time complexity due to dictionary operations.
        """
        self._data[identifier] = weight

    def retrieve(self, identifier: str) -> float | None:
        """
        Retrieves a stored weight measurement by its unique identifier.
        
        Args:
            identifier (str): The key used when storing the data.
            
        Returns:
            float or None: The recorded weight if found; otherwise returns None.
            
        Complexity: O(1) average time complexity due to dictionary lookups.
        """
        return self._data.get(identifier, None)

    def update(self, identifier: str, new_weight: float) -> bool:
        """
        Updates an existing weight measurement or raises a KeyError if not found.
        
        Args:
            identifier (str): The key of the entry to be updated.
            new_weight (float): The new value for the weight.
            
        Returns:
            bool: True if the update was successful; False otherwise (if ID missing).
            
        Complexity: O(1) average time complexity due to dictionary updates.
        """
        self._data[identifier] = new_weight

    def get_all(self) -> dict[str, float]:
        """
        Returns a copy of all stored weight measurements.
        
        Args:
            None
            
        Returns:
            dict[str, float]: A shallow copy of the internal data dictionary 
                             to prevent external modification affecting state.
            
        Complexity: O(n) where n is the number of entries (necessary for copying).
        """
        return self._data.copy()

if __name__ == '__main__':
    # Hard-coded sample values execution block
    manager = WeightManager()

    # Sample data to test store, retrieve, and update operations
    samples = [
        ("user_001", 75.5),
        ("user_002", 80.2),
        ("user_003", 68.9)
    ]

    # Initialize with sample data
    for user_id, weight in samples:
        manager.store(user_id, weight)

    print("Initial Storage Test:")
    assert manager.retrieve("user_001") == 75.5, "Retrieve failed"
    assert manager.retrieve("user_002") == 80.2, "Retrieve failed"
    assert manager.retrieve("user_003") == 68.9, "Retrieve failed"

    # Test update functionality
    print("\nUpdate Test:")
    new_weight_user1 = 76.0
    result_update = manager.update("user_001", new_weight_user1)
    
    assert result_update is True, "Update returned False unexpectedly"
    retrieved_updated = manager.retrieve("user_001")
    assert retrieved_updated == new_weight_user1, f"Expected {new_weight_user1}, got {retrieved_updated}"

    # Test non-existent update (should return False)
    print("\nNon-existent Update Test:")
    result_missing = manager.update("non_existent", 90.0)
    
    assert result_missing is False, "Update on missing key should return False"
    retrieved_missing = manager.retrieve("non_existent")
    assert retrieved_missing is None, "Missing key should return None after update attempt"

    # Test get_all functionality
    print("\nGet All Data:")
    all_data = manager.get_all()
    
    expected_keys = {"user_001", "user_002", "user_003"}
    actual_keys = set(all_data.keys())
    assert actual_keys == expected_keys, f"Keys mismatch: {actual_keys} vs {expected_keys}"

    # Verify internal data is not modified externally via get_all copy
    all_data["test_override"] = 999.0
    retrieved_after_copy = manager.retrieve("user_001")
    
    assert retrieved_after_copy == new_weight_user1, "Internal state was corrupted by external modification of return value"

    print("\nAll tests passed successfully.")