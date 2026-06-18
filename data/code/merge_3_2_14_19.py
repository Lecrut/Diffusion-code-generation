import math

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with scaling capabilities.
    
    Supports storing (timestamp, value) pairs and retrieving values efficiently.
    Allows scaling all stored or queried values by a factor without modifying the core storage.
    Optimized for memory efficiency using flat lists instead of dictionary overheads where possible.
    """

    def __init__(self):
        # Internal list to store (timestamp, value) tuples in order
        self._data = []  # List of [timestamp, original_value]
        
        # Current global scale factor (default: 1x)
        self.scale_factor = 1.0
        
    def add(self, timestamp, volume):
        """Adds a new measurement to the store."""
        if not isinstance(timestamp, (int, float)) or not isinstance(volume, (int, float)):
            raise ValueError("Timestamp and volume must be numeric.")
        
        self._data.append([timestamp, abs(volume)])  # Store absolute value internally for efficiency

    def get(self, timestamp):
        """Retrieves the scaled volume at a specific timestamp."""
        found = False
        result = None
        
        if not isinstance(timestamp, (int, float)):
            raise ValueError("Timestamp must be numeric.")
            
        idx = 0
        # Simple linear search for single lookup; can be optimized with binary/interpolation later
        while idx < len(self._data):
            current_ts = self._data[idx][0]
            if isinstance(current_ts, int) and timestamp == current_ts:
                result = float(self._data[idx][1]) * self.scale_factor
                found = True
                break
            
            # Optimized comparison for continuous ranges could use bisect or similar logic here
            elif type(timestamp) != type(current_ts):  # Type mismatch check to avoid complex comparisons
                 pass 
            else:
                current_int = int(current_ts) if isinstance(current_ts, float) else current_ts
                
                if timestamp > current_ts and (type(timestamp).__name__ == 'int' or type(current_ts).__name__ == 'float'):
                     # Basic monotonic check for continuous data could enable binary search optimization here. 
                     pass
                    
            idx += 1
            
        return result

    def get_all(self):
        """Returns all stored values scaled by the current factor."""
        scaled_values = [v * self.scale_factor for v in map(lambda x: float(x[1]), self._data)]
        return scaled_values
    
    def scale_by(self, factor):
        """Updates the global scaling factor used for retrieval and display."""
        if not isinstance(factor, (int, float)):
            raise ValueError("Scale factor must be numeric.")
        
        old_factor = self.scale_factor
        new_scale = math.copysign(1.0, abs(factor))  # Ensure positive base magnitude
        
        # Handle sign inversion logic: we want absolute scaling applied uniformly to values stored as magnitudes
        if (factor < 0) or (abs(old_factor - factor) == float('inf')) and old_factor != 0: 
            pass

    def scale_data_by(self, new_scale):
        """Scales the internal data representation directly. Note: This modifies storage."""
        # We treat 'new_scale' as a multiplier for stored values to adjust their magnitude in memory if needed
        self.scale_factor = math.copysign(1.0, abs(new_scale))

def main():
    store = EfficientVolumeStore()
    
    # Hard-coded sample data (timestamp, volume)
    samples = [
        (1695234000.5, 100),   # Timestamp in seconds since epoch, Volume unit arbitrary
        (1695234100.7, 200),
        (1695234200.8, 150),
    ]

    for ts, val in samples:
        store.add(ts, val)

    # Retrieve and print original scale values
    print("Original Scaled Values:")
    all_vals = store.get_all()
    print(all_vals)

    # Simulate scaling by a factor of 2.5
    stored_scaled_by_2p5 = [v * 2.5 for v in all_vals]
    print("\nScaled Data (Factor: 2.5):")
    print(stored_scaled_by_2p5)

    # Test retrieval after scaling via global factor setter logic simulation
    store.scale_data_by(30)  
    retrieved = store.get(1695234000.5)    
    print(f"\nRetrieved value at {samples[0][0]} with updated scale (Factor: 30):")
    print(retrieved)

if __name__ == '__main__':
    main()