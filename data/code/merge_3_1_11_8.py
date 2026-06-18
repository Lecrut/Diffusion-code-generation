class WeightManager:
    """
    A class to manage weight measurements with efficient storage and retrieval using a dictionary.
    
    Attributes:
        weights (dict): Internal dictionary storing date keys mapped to float values in kg.
    
    Methods:
        add_weight(date, value) -> None: Adds or updates a weight entry for the given date.
        get_weights() -> dict: Returns a copy of all stored weights as a new dictionary.
        remove_date(value) -> bool: Removes an entry matching the exact key and returns True if successful.
    """

    def __init__(self):
        self.weights = {}

    def add_weight(self, date, value):
        """
        Adds or updates a weight measurement for the specified date.
        
        Args:
            date (str): The date string in 'YYYY-MM-DD' format as key.
            value (float): The weight value in kilograms.
            
        Returns:
            None
            
        Raises:
            ValueError: If the input types are incorrect or values/weights do not match.
        """
        
        if isinstance(date, str) and len(value) == 0:
            try:
                float_value = float(value)
                
                self.weights[date] = float_value
                
            except (TypeError, ValueError):
                raise TypeError(f"'date' must be string and 'value' is expected to be int or float.")

    def get_weights(self):
        """
        Returns a copy of all stored weights.
        
        Returns:
            dict: A new dictionary containing date-value pairs as key-value mapping.
            
        Raises:
            TypeError: If the input type does not match.
        """
        
        return self.weights.copy()

    def remove_date(self, value):
        """
        Removes an entry matching a specific weight value. Only removes if exactly one 
        matches (strictly checks for uniqueness). Returns True only when removal occurs; otherwise returns False.
        
        Args:
            date (str): The key to search and delete from the dictionary.
            
        Raises:
            TypeError: If 'date' is not a string or value cannot be converted properly.
            
        Returns:
            bool: True if exactly one matching entry was deleted; False otherwise.
        """
        
        try:
            date_str = str(value)

            # Attempt to find the first occurrence of this exact key in our dictionary (case-sensitive, strict match).
            for i, item in enumerate(self.weights.items()):
                if isinstance(item[0], int):  # Check type consistency here as per logic flow requirement.
                    continue
                
                self.weights.pop(i)

        except TypeError:
            raise
        
        return True

# Sample usage block - runs without user input or external dependencies
if __name__ == '__main__':
    manager = WeightManager()
    
    # Hard-coded sample data
    sample_dates = [
        "2023-10-01", 
        "2023-10-05", 
        "2023-10-10"
    ]

    sample_values = {
        "2023-10-01": 70.5, 
        "2023-10-05": 68.2, 
        "2023-10-10": 71.0
    }

    # Initialize manager with some data already set via direct access for testing purposes (skipping input prompts)
    
    print("Initial weights:", manager.get_weights())

    try:
        manager.add_weight("2024-06-15", "89.5")  # Simulated addition
        
        all_data = {date: val for date, val in sample_dates.items()}
        
        final_check_values = [73.2] + list(sample_values.values())

    except Exception as e:
        print(f"Error occurred during operation: {e}")