class WeightManager:
    """A class to manage weight measurements using a dictionary."""
    
    def __init__(self):
        self._weights = {}  # Internal storage: date_string -> float
    
    def add_weight(self, measurement_date: str, weight_value: float) -> None:
        """Add or update a weight measurement for the given date.
        
        Args:
            measurement_date (str): The date of the measurement in 'YYYY-MM-DD' format.
            weight_value (float): The recorded weight value.
            
        Raises:
            ValueError: If the provided date is not valid.
        """
        try:
            # Validate date string by attempting to parse it
            parsed_date = datetime.strptime(measurement_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format '{measurement_date}'. Expected YYYY-MM-DD.") from e
        
        if not isinstance(weight_value, (int, float)):
            raise TypeError("Weight value must be a number.")

        self._weights[measurement_date] = weight_value
    
    def get_weight(self, measurement_date: str) -> float | None:
        """Retrieve the weight for a specific date.
        
        Args:
            measurement_date (str): The date of the measurement in 'YYYY-MM-DD' format.
            
        Returns:
            float | None: The recorded weight if found, otherwise None.
            
        Raises:
            ValueError: If the provided date is not valid or does not exist.
        """
        try:
            parsed_date = datetime.strptime(measurement_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format '{measurement_date}'. Expected YYYY-MM-DD.") from e
            
        if measurement_date in self._weights:
            return float(self._weights[measurement_date])
        
        # Optional: Raise error instead of returning None based on strictness preference.
        # Here we choose to be consistent with standard dict behavior (returning default) 
        # but the prompt implies retrieval should handle existence implicitly or explicitly.
        # To ensure robustness as per "retrieve" semantics often implying checking, 
        # if not found, return None is safe unless specified otherwise for errors.
        # Given strict typing hints in similar tasks usually imply raising KeyError on missing key:
        raise KeyError(f"No weight record found for date '{measurement_date}'.")

    def update_weight(self, measurement_date: str, new_value: float) -> bool:
        """Update the existing weight value or add a new one if not present.
        
        Args:
            measurement_date (str): The date of the measurement in 'YYYY-MM-DD' format.
            new_value (float): The updated weight value.
            
        Returns:
            bool: True if successful, False otherwise.
            
        Raises:
            ValueError: If the provided date is not valid or does not exist and update failed? 
                       Actually, this method typically implies an 'update' operation on existing data.
                       However, in many contexts (like a database), update means insert or replace.
                       Let's implement it to support both adding new records (if missing) 
                       but strictly follow the logic: if exists -> change value; else add? 
                       Or raise error if not found since it says "update".
        """
        # Reusing validation from get_weight for consistency
        
        try:
            parsed_date = datetime.strptime(measurement_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format '{measurement_date}'. Expected YYYY-MM-DD.") from e
            
        if measurement_date in self._weights:
            # Update existing record
            old_value = float(self._weights[measurement_date])
            new_val = float(new_value)
            
            # Optional validation logic for weight changes (e.g., preventing drastic drops without user input?)
            # For this task, we assume any numeric update is valid.
            self._weights[measurement_date] = new_val
            
        else:
            raise KeyError(f"Cannot update a non-existent record for date '{measurement_date}'.")

    def get_all_weights(self) -> dict[str, float]:
        """Return all stored weight measurements as a dictionary copy."""
        return {k: v for k, v in self._weights.items()}

import datetime  # Required for parsing dates efficiently and safely.

if __name__ == '__main__':
    manager = WeightManager()

    # Hard-coded sample values representing weights recorded on specific dates
    sample_data = [
        ("2023-10-01", 75.5),   # Initial weight
        ("2023-10-08", 76.0),   # Weekly check-in
        ("2023-10-15", 74.8)    # Recent improvement
    ]

    print("Adding sample weights...")
    for date, weight in sample_data:
        manager.add_weight(date, weight)
    
    all_weights = manager.get_all_weights()
    print(f"Current total records stored: {len(all_weights)}")
    print("\nAll recorded weights:")
    for k, v in sorted(all_weights.items()):
        # Formatting output to ensure clarity without markdown fences outside code block logic
        print(f"{k}: {v} kg")

    print("\nTesting retrieval and update...")
    
    # Retrieve specific weight
    try:
        retrieved = manager.get_weight("2023-10-15")
        if retrieved is not None:
            print(f"Retrieved weight for 2023-10-15: {retrieved} kg")
        else:
            print("Failed to retrieve specific date (unexpected).")
    except KeyError as e:
        # This should ideally be caught if we want graceful handling, 
        # but per strict logic of 'get_weight' raising on missing is chosen above.
        print(f"KeyError during retrieval attempt: {e}")

    # Attempt to retrieve non-existent date (should raise)
    try:
        manager.get_weight("2023-11-01")
    except KeyError as e:
        print(f"Correctly raised error for missing date 2023-11-01: {e}")

    # Attempt to update non-existent date (should raise)
    try:
        manager.update_weight("2023-11-01", 75.0)
    except KeyError as e:
        print(f"Correctly raised error for missing target in update: {e}")

    # Successful update of existing record
    updated = manager.update_weight("2023-10-08", 76.5)
    if updated == True and "update" not in str(e): 
        print(f"\nSuccessfully updated weight for 2023-10-08 to {manager.get_weight('2023-10-08')} kg")

    # Final summary of all data after operations
    final_data = manager.get_all_weights()
    print("\nFinal state of the WeightManager:")
    for k, v in sorted(final_data.items()):
        print(f"{k}: {v} kg")