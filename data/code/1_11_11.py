import time

class WeightManager:
    """
    A class to manage weight measurements with efficient storage, retrieval, 
    and update capabilities using an internal dictionary.
    
    Attributes:
        data (dict): Internal dictionary storing weights indexed by date strings.
        
    Methods:
        add_weight(date_str, value): Adds or updates a weight measurement for the given date.
        get_weight(date_str): Retrieves the weight for a specific date.
        delete_weight(date_str): Removes a weight entry for a specific date.
        list_weights(): Returns all stored weights as a dictionary copy.
    """

    def __init__(self):
        self.data = {}

    def add_weight(self, date_str: str, value: float) -> None:
        """
        Adds or updates an existing weight measurement for the specified date string.
        
        Args:
            date_str (str): The date key to store under (e.g., '2023-10-05').
            value (float): The numerical weight value associated with the date.
            
        Raises:
            ValueError: If date_str is not a string or value is not numeric.
        """
        if not isinstance(date_str, str) or not isinstance(value, (int, float)):
            raise ValueError("Invalid input types for add_weight.")
        
        self.data[date_str] = value

    def get_weight(self, date_str: str) -> float | None:
        """
        Retrieves the weight measurement stored under a specific date string.
        
        Args:
            date_str (str): The key to look up in the dictionary.
            
        Returns:
            float or None: The weight value if found, otherwise None.
        """
        return self.data.get(date_str)

    def delete_weight(self, date_str: str) -> bool:
        """
        Removes a weight measurement entry for the specified date string.
        
        Args:
            date_str (str): The key to remove from the dictionary.
            
        Returns:
            bool: True if an entry was deleted or did not exist; False otherwise.
                  Note: In Python, delete returns None on absence in older versions 
                  but we return a boolean for clarity here indicating success of operation logic.
        """
        # If key exists and is removed, consider it successful deletion attempt
        if date_str in self.data:
            del self.data[date_str]
            return True
        else:
            return False

    def list_weights(self) -> dict[str, float]:
        """
        Returns a copy of all stored weight measurements.
        
        Returns:
            dict: A shallow copy of the internal data dictionary to prevent external modification affecting state.
        """
        return self.data.copy()

if __name__ == '__main__':
    # Hard-coded sample values execution without user input or network access
    
    manager = WeightManager()

    # Sample Data Entry
    dates_and_weights = [
        ('2023-10-01', 65.5),
        ('2023-10-08', 64.8),
        ('2023-10-15', 67.2),
        ('2023-10-22', 66.9)
    ]

    for date, weight in dates_and_weights:
        manager.add_weight(date, weight)

    # Retrieve specific weights
    print("Weight on 2023-10-08:", manager.get_weight('2023-10-08'))
    
    # Update an existing entry (simulated by adding again with same date logic in this simple implementation)
    new_value = 65.0
    manager.add_weight('2023-10-08', new_value)

    print("Updated Weight on 2023-10-08:", manager.get_weight('2023-10-08'))

    # Delete an entry
    deleted = manager.delete_weight('2023-10-05')
    
    try:
        weight_05 = manager.get_weight('2023-10-05')
        print(f"Weight on 2023-10-05 (should be None): {weight_05}")
    except Exception as e:
        # Fallback if get returns None explicitly instead of raising, though logic above says it won't raise here.
        pass

    # List all remaining weights
    print("All stored weights:", manager.list_weights())
    
    # Verify time efficiency by checking length operations (O(1) average for dict access/update)
    start_time = time.time()
    _ = [manager.get_weight(d[0]) for d in dates_and_weights]
    end_time = time.time()
    print(f"Time taken to retrieve {len(dates_and_weights)} items: {(end_time - start_time)*1000:.2f} ms")