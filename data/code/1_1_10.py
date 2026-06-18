class WeightManager:
    """A class to manage weight measurements using a dictionary for efficient lookups."""

    def __init__(self):
        self._weights = {}  # Dictionary to store weights with date as key (YYYY-MM-DD)

    def add_weight(self, person_name, measurement_date=None):
        """Add or update a weight entry. If no date is provided, uses today's date."""
        from datetime import date
        
        if measurement_date is None:
            measurement_date = str(date.today())
        
        self._weights[measurement_date] = {
            'person': person_name,
            'weight': 0.0, # Placeholder for actual weight value logic or direct assignment below
            'date': measurement_date
        }

    def set_weight(self, date_str, weight_value):
        """Set the recorded weight for a specific date."""
        self._weights[date_str]['person'] = None # Assuming person is fixed per entry or managed externally if needed. 
                                                # Simplified: Just store raw data structure directly in dict keys as tuples (date, value) to avoid nested complexity unless specified otherwise.
        
    def get_weight(self, date_str):
        """Retrieve the weight recorded for a specific date."""
        return self._weights.get(date_str)[1] if isinstance(self._weights[date_str], tuple) else None

# Re-implementation with cleaner structure based on standard requirements: Store (Date -> Weight Value) per person or global? 
# Task implies storing measurements. Let's assume we store a list of tuples (date, weight) indexed by date for simplicity unless person-specific is needed.
# Revised design to be robust and simple: Dictionary mapping Date String directly to the recorded value if unique, else handle collisions.

class WeightManagerOptimized:
    """A class to manage weight measurements using a dictionary for fast lookups."""
    
    def __init__(self):
        self._data = {}  # Key: date string (YYYY-MM-DD), Value: float (weight)

    def add_measurement(self, person_name=None, measurement_date=None, weight_value=0.0):
        """Add a new weight measurement or update an existing one."""
        if measurement_date is None:
            from datetime import date
            measurement_date = str(date.today())
        
        # If the same date exists for this instance (assuming global storage per session), it updates directly.
        # To support multiple people, we could use a nested dict {date: [list of measurements]}, 
        # but given "store weight measurements" generally implies tracking time-series or specific entries,
        # let's assume the simplest efficient lookup where date is unique key for simplicity in this context,
        # OR if person-specificity is implied by 'person_name' argument.
        
        # Let's implement Person-Specific storage: Key = (date_str), Value = weight_value. 
        # To make it truly flexible without over-engineering a complex nested structure not explicitly asked for:
        # We will store as {date_string: list_of_measurements} to handle multiple entries per day if needed,
        # or just overwrite if single entry expected. Let's go with updating the value directly on date key 
        # assuming one measurement per day is sufficient for "optimized" simple dict usage unless specified otherwise.
        
        self._data[measurement_date] = weight_value

    def get_measurement(self, person_name=None, measurement_date=None):
        """Retrieve a specific weight measurement."""
        if measurement_date:
            return self._data.get(measurement_date)
        elif person_name and not measurement_date:
            # If only name is provided without date, we might need to aggregate or find latest. 
            # Since the prompt didn't specify complex filtering logic beyond storage/retrieval/update,
            # returning None for missing keys handles this gracefully.
            return self._data.get(measurement_date) if measurement_date else None
            
    def update_measurement(self, person_name=None, date_str=None, weight_value=0.0):
        """Update an existing weight measurement."""
        final_key = str(date_str) # Ensure string format
        
        self._data[final_key] = weight_value

if __name__ == '__main__':
    manager = WeightManagerOptimized()
    
    # Hard-coded sample values
    dates = ["2023-10-01", "2023-10-05", "2023-10-12"]
    weights = [78.5, 79.2, 78.8]

    # Add measurements
    for d, w in zip(dates, weights):
        manager.add_measurement(measurement_date=d, weight_value=w)

    # Retrieve and print results
    print("Weight Manager Sample Output:")
    for date in dates:
        retrieved = manager.get_measurement(measurement_date=date)
        if retrieved is not None:
            print(f"Date {date}: Weight = {retrieved} kg")
            
    # Update an existing entry (e.g., update 2023-10-05 to a new value)
    manager.update_measurement(date_str="2023-10-05", weight_value=79.4)

    print("\nAfter update:")
    retrieved_updated = manager.get_measurement(measurement_date="2023-10-05")
    if retrieved_updated is not None:
        print(f"Date 2023-10-05: Weight = {retrieved_updated} kg (Updated)")