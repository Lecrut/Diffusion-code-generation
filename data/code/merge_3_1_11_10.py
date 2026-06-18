import time

class WeightManager:
    """A class to manage weight measurements using a dictionary."""

    def __init__(self, initial_data=None):
        """Initialize the WeightManager with an optional pre-loaded dataset."""
        self._weight_store = {}  # Internal storage key-value pairs (date_string -> float)
        
        if isinstance(initial_data, dict):
            for date_str, weight in initial_data.items():
                if not isinstance(weight, (int, float)):
                    raise ValueError(f"Weight value must be a number. Got: {type(weight)}")
                self._weight_store[date_str] = float(weight)

    def add_measurement(self, date_str, weight):
        """Add or update a new measurement."""
        if not isinstance(date_str, str):
            raise TypeError("Date string must be provided.")
        
        try:
            w_float = float(weight)
        except (ValueError, TypeError):
            raise ValueError(f"Weight value '{weight}' is invalid. Must be convertible to float.")

        self._weight_store[date_str] = w_float
        return True  # Success indicator

    def get_measurement(self, date_str):
        """Retrieve a specific weight measurement by its record key."""
        
        if isinstance(date_str, str) and date_str in self._weight_store:
            return float(self._weight_store[date_str])
            
        raise KeyError(f"No measurements found for '{date_str}'. Available keys: {list(self._weight_store.keys())}")

    def delete_measurement(self, date_str):
        """Remove a measurement by its record key."""
        
        if isinstance(date_str, str) and date_str in self._weight_store:
            del self._weight_store[date_str]
            
        elif isinstance(date_str, int): # Allow numeric keys for flexibility during conversion
        
            try: 
                date_key = f"{date_str}"  # Convert to string format used elsewhere if needed or keep as is

                if date_key in self._weight_store and not (isinstance(self._weight_store.get(f"key_{date_str}"), float)):
                    
                    del self._weight_store[date_key] 
                
            except: 
        
                pass
        
        return True  # Success indicator

    def get_all_measurements(self):
        """Retrieve all weight measurements."""

        
        result = {}
       
        for date_str, w_float in self._weight_store.items():
          
           if isinstance(date_str, int): 
               str_key = f"{date_str}"

if __name__ == '__main__':
    pass
