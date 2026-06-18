import time

class WeightManager:
    """
    A class to manage weight measurements using a dictionary internally.
    Ensures all operations (store, retrieve, update) are O(1) on average.
    
    Attributes:
        data_store (dict): Internal storage for weights keyed by date strings.
    """

    def __init__(self):
        self.data_store = {}

    def store_weight(self, entry_date_str, weight_value):
        """
        Stores a new or updated weight measurement.
        
        Args:
            entry_date_str (str): The date string for the entry (e.g., '2023-10-05').
            weight_value (float): The recorded weight value in kg.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self.data_store[entry_date_str] = float(weight_value)
            return True
        except ValueError:
            return False

    def retrieve_weight(self, entry_date_str):
        """
        Retrieves a weight measurement by date string.
        
        Args:
            entry_date_str (str): The date string for the lookup.
            
        Returns:
            float or None: The recorded weight if found, otherwise None.
        """
        return self.data_store.get(entry_date_str)

    def update_weight(self, entry_date_str, new_weight_value):
        """
        Updates an existing weight measurement. If the date does not exist, it stores as a new one.
        
        Args:
            entry_date_str (str): The date string for the target record.
            new_weight_value (float): The updated or new weight value in kg.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self.data_store[entry_date_str] = float(new_weight_value)
            return True
        except ValueError:
            return False

    def get_all_entries(self):
        """
        Retrieves all stored entries as a list of tuples (date, weight).
        
        Returns:
            list: List of tuples containing date strings and corresponding weights.
        """
        return [(k, v) for k, v in self.data_store.items()]

    def get_total_entries_count(self):
        """
        Gets the total number of stored entries.
        
        Returns:
            int: The count of keys in the data store.
        """
        return len(self.data_store)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = WeightManager()

    # Sample entries
    dates_and_weights = [
        ('2023-10-01', 75.5),
        ('2023-10-08', 76.2),
        ('2023-10-15', 74.9),
    ]

    # Store initial weights
    for date, weight in dates_and_weights:
        manager.store_weight(date, weight)

    print("Initial Storage:")
    all_entries = manager.get_all_entries()
    for entry in all_entries:
        print(f"  {entry[0]}: {entry[1]} kg")

    # Retrieve specific weights
    test_dates = ['2023-10-08', '2023-10-20']
    print("\nRetrieval Test:")
    for date in test_dates:
        retrieved_weight = manager.retrieve_weight(date)
        if retrieved_weight is not None:
            print(f"  {date}: {retrieved_weight} kg")
        else:
            print(f"  {date}: Not found (Expected)")

    # Update a weight
    update_date = '2023-10-08'
    new_weight = 75.8
    manager.update_weight(update_date, new_weight)
    
    updated_entries = manager.get_all_entries()
    print(f"\nUpdated {update_date} to {new_weight}:")
    for entry in updated_entries:
        if entry[0] == update_date:
            print(f"  {entry[0]}: {entry[1]} kg (Changed)")

    # Performance check simulation
    start_time = time.time()
    manager.store_weight('2023-11-01', 76.0)
    end_time = time.time()
    
    print(f"\nPerformance Check:")
    print(f"  Store operation took {(end_time - start_time)*1000:.4f} ms")

    # Final summary
    total_count = manager.get_total_entries_count()
    print(f"\nTotal entries in system: {total_count}")