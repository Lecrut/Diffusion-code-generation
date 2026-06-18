import math
from typing import List, Optional, Tuple

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support for 
    scaling by a given factor while maintaining memory efficiency and fast retrieval.
    
    Uses floating-point arithmetic internally but supports arbitrary scale factors.
    Implements O(1) average time complexity for insertion, update, and retrieval of values.
    """

    def __init__(self):
        # Internal storage: list of (value_index, scaled_value) tuples to avoid 
        # storing redundant data if multiple scales are used simultaneously.
        self._data_store: List[Tuple[int, float]] = []  # Stores raw value index and pre-scaled values for common factors? No, simpler approach below.
        
        # To ensure memory efficiency regardless of scale factor usage pattern, 
        # we store the base volume data once and compute scaled versions on demand or cache them if needed.
        # However, since scaling is dynamic per query/request (not necessarily pre-known),
        # storing raw values only ensures minimal memory footprint until a specific scale is requested.

        self._raw_values: List[float] = []  # Stores original volume measurements
        
    def add_volume(self, value: float) -> None:
        """Adds a new volume measurement to the store."""
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be numeric.")
        
        self._raw_values.append(float(value))

    def get_scaled_value(self, index: int, scale_factor: float) -> Optional[float]:
        """
        Retrieves a volume value scaled by the given factor.
        
        Args:
            index (int): Index of the measurement in raw values list.
            scale_factor (float): Factor to multiply the original value by.
            
        Returns:
            Scaled float or None if index out of bounds.
        """
        if not isinstance(index, int) or not isinstance(scale_factor, (int, float)):
            raise TypeError("Index must be integer and scale factor numeric.")

        if 0 <= index < len(self._raw_values):
            return self._raw_values[index] * scale_factor
        
        return None

    def get_all_scaled(
        self, 
        start_index: int = 0, 
        end_index: Optional[int] = None, 
        scale_factor: float = 1.0
    ) -> List[float]:
        """
        Retrieves a slice of volume values scaled by the given factor efficiently.
        
        Args:
            start_index (int): Start index for slicing.
            end_index (Optional[int]): End index for slicing (exclusive). If None, goes to end.
            scale_factor (float): Factor to multiply each value by.
            
        Returns:
            List of scaled floats.
        """
        if not isinstance(start_index, int) or not isinstance(scale_factor, (int, float)):
            raise TypeError("Indices and scale factor must be numeric.")

        end = len(self._raw_values) if end_index is None else min(end_index, len(self._raw_values))
        
        return [self.get_scaled_value(i, scale_factor) for i in range(start_index, end)]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.

    store = EfficientVolumeStore()

    # Simulate adding some volume data points (e.g., liters per hour over time)
    raw_data_points = [10, 25, 30, 45, 60]
    
    for val in raw_data_points:
        store.add_volume(val)

    print("Original Data Points:", store._raw_values)

    # Retrieve a specific value scaled by factor of 1.5 (e.g., converting to gallons approx or arbitrary unit scaling)
    index_to_check = 2
    scale_factor_1p5 = 1.5
    
    result_scaled = store.get_scaled_value(index_to_check, scale_factor_1p5)
    
    print(f"Value at index {index_to_check} scaled by {scale_factor_1p5}:", result_scaled)

    # Retrieve a slice of data points scaled differently (e.g., factor 0.1 for milliliters approximation logic if input was liters)
    start_idx = 1
    end_idx = None
    scale_factor_small = 0.1
    
    sliced_data = store.get_all_scaled(start_index=start_idx, end_index=end_idx, scale_factor=scale_factor_small)

    print(f"Sliced data from index {start_idx} to {end}, scaled by {scale_factor_small}:", sliced_data)

    # Demonstrate memory efficiency: we only stored raw values. No redundant copies were made unless explicitly requested via slicing or scaling on demand.
    
    # Test edge cases
    
    try:
        store.get_scaled_value(-1, 2.0)
    except Exception as e:
        print("Expected error for negative index:", type(e).__name__)

    try:
        store.add_volume("invalid")
    except TypeError as te:
        print("Expected Type Error for non-numeric input:", str(te))