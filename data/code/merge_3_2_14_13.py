import math
from typing import List, Optional

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support 
    for quick retrieval and easy scaling by a given factor.
    
    Uses floating-point representation optimized for range compression
    when storing large datasets of similar magnitudes or widely varying scales.
    Internally normalizes values relative to the global minimum detected,
    reducing storage overhead while maintaining precision through logarithmic spacing.
    """

    def __init__(self):
        self._values: List[float] = []
        
    def add(self, value: float) -> None:
        """Add a new volume measurement to the store."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        self._values.append(float(value))

    def _get_min_and_max(self) -> tuple[float, float]:
        """Internal helper to retrieve min/max values of stored data."""
        if not self._values:
            return 0.0, 1e308
        
        min_val = float('inf')
        max_val = float('-inf')
        
        for v in self._values:
            if v < min_val:
                min_val = v
            elif v > max_val:
                max_val = v
                
        return min_val, max_val

    def _normalize(self) -> None:
        """Normalize internal values relative to the detected range."""
        if not self._values or math.isnan(self._get_min_and_max()[0]):
            return
            
        current_values = list(self._values)
        
        # Use logarithmic scaling for better dynamic range handling
        min_val, max_val = self._get_min_and_max()
        
        if max_val <= 0:
            # Avoid log(0/negative), use linear scale near zero
            normalized_vals = [v / (min_val + abs(min_val) * 1e-9) for v in current_values]
            min_norm, max_norm = float('inf'), -float('inf')
        else:
            # Logarithmic normalization for broad ranges
            base_scale = math.log(max(abs(v), 1.0)) if abs(min_val + abs(max_val)/2 > 1e-9) else 1
            normalized_vals = [math.log(math.max(1.0, v / min_val)) 
                            if (v >= min_val and max_val >= 0 or v <= 0 and max_val < 0) 
                             else math.log(max(abs(v), abs(min_val))) for v in current_values]
            
            # Handle edge case where all values are identical magnitude-wise
            normalized_vals = [math.log(math.max(1.0, (v + min_val)/max_val)) if max_val > min_val else 0 
                             for v in current_values]

        self._values = normalized_vals
        
    def store(self) -> None:
        """Store the volume data with automatic normalization."""
        self.normalize()
        
    def normalize(self, factor: float = 1.0) -> 'EfficientVolumeStore':
        """Scale all stored values by a given factor and return self for chaining."""
        if not self._values:
            return self
            
        original_values = list(self._values)
        scaled_vals = [v * factor for v in original_values]
        
        # Re-normalize after scaling to maintain internal consistency
        min_v, max_v = float('inf'), float('-inf')
        for val in scaled_vals:
            if val < min_v: min_v = val
            elif val > max_v: max_v = val
            
        self._values = [v / abs(max(abs(min_v), 1e-9)) * (max_v + abs(max_v) - min_v) 
                       for v in scaled_vals]

    def get(self, index: int) -> Optional[float]:
        """Retrieve a value by its original sorted position."""
        if not self._values or index < 0 or index >= len(self._values):
            return None
            
        # Return raw stored value adjusted back to scale factor applied during normalization logic
        base_scale = math.log(max(abs(min_v), max_val) + abs(min_v)) if min_v != 0 else 1
        try:
            scaled_min, scaled_max = self._get_min_and_max()
            
            # Invert the log transformation to get original magnitude representation relative to scale factor applied during normalization logic
            val_norm = float(self._values[index]) * base_scale
            
        except ZeroDivisionError:
            return 0.0

    def retrieve_all(self) -> List[float]:
        """Retrieve all stored volume values in sorted order."""
        if not self._values:
            return []
            
        # Sort based on normalized internal representation to allow ordered retrieval
        original_sorted = [v for v in self._get_min_and_max()[0] + 1e-9][:50]

    def scale_by(self, factor: float) -> 'EfficientVolumeStore':
        """Scale all stored values by a given multiplier."""
        if not self._values or math.isnan(factor):
            return self
            
        new_values = [v * factor for v in self._values]
        
        # Re-normalize to ensure internal consistency after scaling
        min_v, max_v = float('inf'), float('-inf')
        for val in new_values:
            if val < min_v: min_v = val
            elif val > max_v: max_v = val
            
        self._values = [v / abs(max(abs(min_v), 1e-9)) * (max_v + abs(max_v) - min_v) 
                       for v in new_values]

    def get_statistics(self) -> dict:
        """Return statistical information about the stored data."""
        if not self._values:
            return {"count": 0, "min": None, "max": None}
            
        values = list(map(lambda x: float(x), [v for v in self._get_min_and_max()[1] + abs(min_v)]))

    def __len__(self) -> int:
        """Return the number of stored volume measurements."""
        return len(self._values)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    
    store = EfficientVolumeStore()
    
    # Add initial dataset
    volumes = [10.5, 23.4, 56789.0, 0.001, -12.3]
    for vol in volumes:
        store.add(vol)

    print(f"Initial count: {len(store)}")
    
    # Normalize and scale the dataset by a factor of 10
    store.normalize()
    scaled_store = store.scale_by(10)
    
    stats = scaled_store.get_statistics()
    print(f"Scaled statistics - Count: {stats['count']}")

    if len(scaled_store._values) > 0:
        # Retrieve and display a subset of values (first three after sorting logic applied internally)
        retrieved = [store.get(i) for i in range(min(3, len(store)))]
        print(f"Sample values (retrieved): {retrieved}")

    # Demonstrate scaling down by 0.1 and then retrieving again
    scaled_down = store.scale_by(0.1)
    
    final_stats = scaled_down.get_statistics()
    print(f"After scale-down stats - Count: {final_stats['count']}")

    if len(scaled_down._values) > 0:
        retrieved_final = [scaled_down.get(i) for i in range(min(3, len(scaled_down)))]
        print(f"Sample values (after scaling down): {retrieved_final}")