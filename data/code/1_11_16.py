import time

class WeightManager:
    """
    A class to manage weight measurements using a dictionary internally.
    Ensures O(1) average time complexity for store, retrieve, and update operations.
    
    Attributes:
        data (dict): Internal storage mapping dates/IDs to weights in kg.
    """

    def __init__(self):
        self.data = {}

    def add_weight(self, date_str: str, weight_kg: float) -> None:
        """
        Adds or updates a weight measurement for the given date string.
        
        Args:
            date_str (str): The date key in 'YYYY-MM-DD' format.
            weight_kg (float): The weight value to store.
            
        Returns:
            None
            
        Complexity: O(1) average time.
        """
        self.data[date_str] = weight_kg

    def get_weight(self, date_str: str) -> float | None:
        """
        Retrieves the weight measurement for a specific date string if it exists.
        
        Args:
            date_str (str): The date key in 'YYYY-MM-DD' format.
            
        Returns:
            float or None: The recorded weight, or None if not found.
            
        Complexity: O(1) average time.
        """
        return self.data.get(date_str)

    def update_weight(self, date_str: str, new_weight_kg: float) -> bool:
        """
        Updates the existing weight measurement for a given date string.
        
        Args:
            date_str (str): The date key in 'YYYY-MM-DD' format.
            new_weight_kg (float): The updated weight value.
            
        Returns:
            bool: True if update was successful, False otherwise.
            
        Complexity: O(1) average time.
        """
        self.data[date_str] = new_weight_kg
        return True

    def get_average(self) -> float | None:
        """
        Calculates and returns the average weight across all recorded entries.
        
        Returns:
            float or None: The average weight, or None if no data exists.
            
        Complexity: O(n), where n is the number of records.
        """
        if not self.data:
            return None
        
        total = sum(self.data.values())
        count = len(self.data)
        return round(total / count, 2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = WeightManager()

    # Adding initial weights
    manager.add_weight("2023-10-01", 75.5)
    manager.add_weight("2023-10-08", 76.0)
    manager.add_weight("2023-10-15", 74.8)

    # Retrieving a specific weight
    retrieved = manager.get_weight("2023-10-15")
    print(f"Weight on 2023-10-15: {retrieved} kg")

    # Updating an existing entry
    updated_successfully = manager.update_weight("2023-10-08", 76.2)
    if updated_successfully:
        print(f"Updated weight for 2023-10-08 to {manager.get_weight('2023-10-08')} kg")

    # Attempting retrieval of non-existent date (should return None)
    missing = manager.get_weight("2023-11-01")
    print(f"Weight on 2023-11-01: {missing}")

    # Calculating average weight over all entries
    avg_wt = manager.get_average()
    if avg_wt is not None:
        print(f"Average weight recorded so far: {avg_wt} kg")
    
    # Simulating a performance check by adding many records and timing retrieval (optional demo)
    start_time = time.perf_counter()
    for i in range(100):
        date_key = f"2023-10-{i+1:02d}"
        manager.add_weight(date_key, 75.0 + (i % 4))
    
    end_time = time.perf_counter()

    # Verify one of the newly added records was stored correctly in O(1)
    test_date = "2023-10-99"
    val = manager.get_weight(test_date)
    print(f"Test record for {test_date}: {val}")
    
    final_avg = manager.get_average()
    if final_avg:
        print(f"Total records processed in demo: {len(manager.data)}, Average weight: {final_avg} kg")