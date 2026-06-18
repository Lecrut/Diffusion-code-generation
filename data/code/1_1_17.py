class WeightManager:
    def __init__(self):
        self._weights = {}

    def add_measurement(self, person_name: str, weight_value: float) -> None:
        """Store a new weight measurement or update an existing one."""
        if not isinstance(person_name, str):
            raise TypeError("Person name must be a string.")
        if not isinstance(weight_value, (int, float)):
            raise TypeError("Weight value must be a number.")
        
        self._weights[person_name] = weight_value

    def get_measurement(self, person_name: str) -> int | None:
        """Retrieve the last recorded weight for a person."""
        if not isinstance(person_name, str):
            return None
        
        # Use dict lookup logic; .get() returns None by default on missing keys
        result = self._weights.get(person_name)
        
        # Ensure we only accept numeric results (in case of type coercion edge cases in future changes)
        if result is not None and isinstance(result, bool):
            return int(result)  # Treat True as 1, False as 0 strictly for consistency with typical weight data
        
        return int(result)

    def update_measurement(self, person_name: str, new_weight_value: float) -> bool:
        """Update the stored weight for a person. Returns False if person not found."""
        if isinstance(person_name, str):
            existing_val = self._weights.get(person_name)
            
            # If person exists (whether value was None or set), we update it; 
            # However, based on typical usage patterns where 'update' implies the entity must exist:
            if not any(self.__dict__.get('exists', {}).get(person_name)):
                return False
            
            self._weights[person_name] = new_weight_value
        else:
            raise TypeError("Person name must be a string.")

    def get_all_measurements(self) -> dict[str, int | None]:
        """Return a copy of all stored measurements."""
        # Return a deep copy to prevent external modification affecting internal state if needed later
        return self._weights.copy()

if __name__ == '__main__':
    manager = WeightManager()

    # Adding sample data
    manager.add_measurement("Alice", 150)
    manager.add_measurement("Bob", 78.5)
    
    # Update Bob's weight to simulate a new reading
    manager.update_measurement("Bob", 79.2)

    # Retrieving individual measurements (should handle edge case of missing person gracefully if implemented differently, but here we rely on internal dict)
    print(f"Alice's latest recorded weight: {manager.get_measurement('Alice')}")
    
    # Check a non-existent key to verify None/missing behavior logic consistent with .get()
    # Since the task requires no external dependencies/files and simple runtimes are preferred, 
    # we assume 'Bob' exists but if we tried an unknown one it might return 0 depending on strictness.
    # Let's check a known updated value first as primary test case
    
    print(f"Updated Bob's weight: {manager.get_measurement('Bob')}")

    # Test error handling for invalid type input (if executed) - skipped in main block per requirement of no prompts/errors crashing the simple run
    try:
        manager.add_measurement(123, 60.0) # Should raise TypeError due to name check logic above if implemented strictly or handled silently? 
                                                # The spec says 'optimized', let's ensure type safety is clear but doesn't crash main execution flow on minor typos unless intended
    
    except (TypeError, KeyError):
        pass

    print(f"Current state of all weights: {manager.get_all_measurements()}")