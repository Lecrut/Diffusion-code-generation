import time

class WeightManager:
    """
    An optimized class to manage weight measurements using an internal dictionary.
    Supports storing, retrieving, updating weights with O(1) average-time complexity.
    
    Attributes:
        data (dict): Internal storage for weight records keyed by date strings.
                     Format: {date_string: float} where value is the recorded weight in kg.
    """

    def __init__(self):
        self.data = {}

    def store_weight(self, entry_date, weight_kg):
        """
        Stores a new or updated weight measurement.
        
        Args:
            entry_date (str): The date of the measurement as a string (e.g., '2023-10-05').
                             Must be unique per key in this implementation for simple lookup,
                             though updates overwrite existing values if duplicate keys occur naturally.
            weight_kg (float or int): The recorded body weight in kilograms.

        Returns:
            bool: True if the operation was successful.
        
        Raises:
            TypeError: If entry_date is not a string or weight_kg is not numeric.
        """
        if not isinstance(entry_date, str) or not isinstance(weight_kg, (int, float)):
            raise TypeError("entry_date must be a string and weight_kg must be numeric.")

        self.data[entry_date] = float(weight_kg)
        return True

    def retrieve_weight(self, entry_date):
        """
        Retrieves the stored weight for a specific date.
        
        Args:
            entry_date (str): The date of the measurement as a string.

        Returns:
            float or None: The recorded body weight in kilograms if found, otherwise None.
        
        Raises:
            KeyError: If the provided entry_date does not exist in internal storage.
                       Note: Using dict.get() is preferred for safety over direct access to avoid exceptions on missing keys.
        """
        # Direct dictionary lookup which returns None automatically if key doesn't exist, avoiding KeyError exception logic overhead unless explicit error handling is desired elsewhere.
        return self.data.get(entry_date)

    def update_weight(self, entry_date, new_weight_kg):
        """
        Updates an existing weight measurement or stores a new one (idempotent behavior).
        
        Args:
            entry_date (str): The date of the original record to be updated.
            new_weight_kg (float or int): The new recorded body weight in kilograms.

        Returns:
            bool: True if an update was performed successfully.
        
        Raises:
            TypeError: If inputs are invalid types.
            
        Note: This method behaves identically to store_weight but is named for clarity regarding modification intent.
        """
        return self.store_weight(entry_date, new_weight_kg)

    def get_all_weights(self):
        """
        Returns a copy of all stored weights as an ordered dictionary (preserving insertion order in Python 3.7+).
        
        Returns:
            dict: A shallow copy of the internal data structure to prevent external modification affecting state.
        """
        return self.data.copy()

    def get_total_entries(self):
        """
        Retrieves the total count of stored weight entries.
        
        Returns:
            int: The number of keys in the dictionary.
        """
        return len(self.data)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    manager = WeightManager()

    # Sample data entries (dates and weights in kg)
    samples = [
        ('2023-10-01', 65.4),
        ('2023-10-08', 66.1),
        ('2023-10-15', 67.0),
    ]

    # Store initial weights
    for date, weight in samples:
        manager.store_weight(date, weight)

    print(f"Total entries stored: {manager.get_total_entries()}")
    
    # Retrieve and verify specific entry
    retrieved = manager.retrieve_weight('2023-10-08')
    if retrieved is not None:
        print(f"Weight on 2023-10-08: {retrieved} kg")
    else:
        print("Weight for 2023-10-08 was not found.")

    # Update an existing entry (simulate a weight change)
    manager.update_weight('2023-10-08', 65.9)
    
    retrieved_updated = manager.retrieve_weight('2023-10-08')
    print(f"Updated Weight on 2023-10-08: {retrieved_updated} kg")

    # Demonstrate retrieval of all data (copy to avoid mutation side effects)
    full_data = manager.get_all_weights()
    
    performance_check_start = time.perf_counter()
    for _ in range(1000):
        manager.retrieve_weight('2023-10-08')
    performance_check_end = time.perf_counter()

    print(f"Time taken for 1000 retrievals: {performance_check_end - performance_check_start:.6f} seconds")