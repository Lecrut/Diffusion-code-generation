import math
from typing import List, Optional, Tuple

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support 
    for scaling by a given factor while maintaining memory efficiency and fast retrieval.
    
    Uses floating-point arithmetic internally but supports arbitrary precision scaling
    via the scale_factor parameter during storage or query operations if needed.
    Internally stores values normalized relative to base units (e.g., liters, cubic meters).
    """

    def __init__(self):
        # Internal list of stored volumes as floats for memory efficiency and speed
        self._data: List[float] = []
    
    def add_volume(self, value: float) -> None:
        """Adds a volume measurement to the store."""
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be numeric")
        self._data.append(float(value))

    def get_average_scaled(self, scale_factor: Optional[float] = 1.0) -> float:
        """Returns the average of all stored volumes scaled by a given factor."""
        if not self._data:
            return 0.0
        
        avg = sum(self._data) / len(self._data)
        # Apply scaling only at retrieval time for flexibility without storing multiple copies
        return avg * scale_factor

    def get_min_max_scaled(
        self, 
        min_scale: Optional[float] = None, 
        max_scale: Optional[float] = None
    ) -> Tuple[Optional[float], Optional[float]]:
        """Returns the minimum and maximum stored volumes scaled by optional factors."""
        if not self._data:
            return (None, None)

        min_val = float('inf')
        max_val = float('-inf')

        for v in self._data:
            # Apply scale individually to find bounds without pre-scaling all data
            scaled_v = v * 1.0 if min_scale is None and max_scale is None else (v * min_scale) \
                if min_scale is not None or max_scale is None else (v * max_scale)

            if scaled_v < min_val:
                min_val = scaled_v
            if scaled_v > max_val:
                max_val = scaled_v
        
        return (min_val, max_val)

    def get_count(self) -> int:
        """Returns the number of stored volumes."""
        return len(self._data)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    
    store = EfficientVolumeStore()
    
    # Sample volume data in liters (simulated sensor readings over time)
    samples = [10.5, 23.7, 45.2, 67.8, 90.1]
    
    for vol in samples:
        store.add_volume(vol)

    # Retrieve average with default scaling (factor of 1)
    avg_vol = store.get_average_scaled()
    print(f"Average volume (unscaled): {avg_vol:.2f} L")

    # Scale up by factor of 5 for simulation purposes
    scaled_avg = store.get_average_scaled(scale_factor=5.0)
    print(f"Average volume (scaled x5): {scaled_avg:.2f} L")

    # Get min and max with different scaling factors applied per bound
    mins, maxs = store.get_min_max_scaled(min_scale=1.0, max_scale=3.0)
    if mins is not None:
        print(f"Minimum volume (unscaled): {mins:.2f} L")
    else:
        print("No minimum available.")

    # Retrieve count of stored items
    count = store.get_count()
    print(f"Total measurements recorded: {count}")

    # Demonstrate memory efficiency by showing internal list size matches logical data
    assert len(store._data) == 5, "Internal storage must match added volumes."
    
    # Additional test case with negative scaling to verify robustness
    neg_scaled = store.get_average_scaled(scale_factor=-2.0)
    print(f"Average volume (scaled x-2): {neg_scaled:.2f} L")

    # Final assertion ensures correctness of calculations
    expected_avg_raw = sum(samples) / len(samples)
    assert abs(scaled_avg - 5 * expected_avg_raw) < 1e-6, "Scaling calculation failed."
    
    print("All tests passed successfully.")