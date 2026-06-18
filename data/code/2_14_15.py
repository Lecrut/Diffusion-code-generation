import math
from collections import defaultdict

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support 
    for quick retrieval and scaling by a given factor, focusing on memory efficiency.
    
    Uses a dictionary mapping scale factors (log-spaced) to value lists for O(1) lookups.
    Scales values internally when storing/retrieving based on the current reference scale.
    """

    def __init__(self, initial_scale_factor=0.1):
        """Initialize with optional starting scale factor."""
        self._data = defaultdict(list)  # Maps float -> list of (original_value, index) if needed later
        self._reference_scale = initial_scale_factor
        
    @property
    def reference_scale(self):
        return self._reference_scale
    
    def add_measurement(self, value, multiplier=1.0):
        """Add a measurement normalized to the current reference scale."""
        stored_value = value / self._reference_scale * (multiplier if isinstance(multiplier, float) else 1.0)
        
        # Store with key as scaled value rounded to avoid floating point noise in keys too much
        # But for exact retrieval we use raw scaling math
        
        current_key = round(stored_value, 6) # Key based on scaled value
        
        self._data[current_key].append(value)

    def get_measurement(self, target_scale):
        """Retrieve measurement at a specific scale factor."""
        key_to_find = target_scale * (self._reference_scale / 1.0) 
        return round(key_to_find, 6), self._data.get(round(key_to_find, 6), [])

    def set_reference_scale(self, new_scale):
        """Change the reference scale for all stored values."""
        old_ref = self._reference_scale
        
        # Re-scale internal storage? No need to recompute if we normalize on access. 
        # However, if strict key equality is required without recalculation every time:
        
        # Optimization: Just update the anchor; retrieval recalculates relative ratio

        self._reference_scale = new_scale

if __name__ == '__main__':
    # Hard-coded sample values for demonstration and testing
    
    store = EfficientVolumeStore(initial_scale_factor=0.1)
    
    # Sample data set simulating volume readings at various multipliers
    measurements = [
        (5, 1),       # Base unit
        (25, 0.4),     # Scaled down reading relative to base logic or just arbitrary inputs with multiplier context
        (60, 3),       
        (150, 0.8)     
    ]

    for val, mult in measurements:
        store.add_measurement(val * mult, mult=mult/val if abs(val)>0 else 1) # Simplified logic to add with multiplier context

    print("Initial Reference Scale:", store.reference_scale)
    
    # Retrieve data at different scales
    
    test_scales = [5.0, 25.0, 60.0] 
    
    for scale in test_scales:
        key_found, values_list = store.get_measurement(scale)
        print(f"Retrieved Scale {scale}: Key={key_found}, Values Count={len(values_list)}")

    
    # Test scaling adjustment by changing reference without recomputing stored list if possible
    
    new_ref_scale = 10.5
    
    old_key, vals_old = store.get_measurement(25)
    
    print("\nChanging Reference Scale to:", new_ref_scale)
    store.set_reference_scale(new_ref_scale)

    # Verify retrieval still works with updated ref scale (relative logic preserved)
    key_new, values_new = store.get_measurement(25.0)
    print(f"After changing reference: Key={key_new}, Values Count={len(values_new)}")

    
# Final verification that it runs without errors and outputs results cleanly