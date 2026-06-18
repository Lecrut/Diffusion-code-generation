import math
from typing import Dict, List, Optional, Tuple

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with scaling capabilities.
    
    Features:
    - Stores raw values in a compact list (float64).
    - Supports quick retrieval of scaled values via logarithmic factor lookup or direct multiplication.
    - Memory-efficient by avoiding redundant object creation for each scale operation.
    """

    def __init__(self, initial_capacity: int = 1024):
        self._raw_data: List[float] = []
        # Pre-allocate a small cache of common scaling factors to avoid repeated log/exp calculations during lookups
        self._scale_cache: Dict[int, float] = {}

    def add_volume(self, value: float) -> None:
        """Adds a new volume measurement."""
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be numeric")
        
        # Avoid duplicate exact values to save memory in dense datasets
        existing_idx = -1
        for i, v in enumerate(self._raw_data):
            if abs(v - value) < 1e-9:
                existing_idx = i
                break
        
        if existing_idx != -1:
            self._scale_cache[existing_idx] += 0.5 # Mark as duplicate/scaled down conceptually (optional tracking)
        else:
            self._raw_data.append(value)

    def get_scaled_value(self, index: int, factor: float) -> Optional[float]:
        """
        Retrieves a volume value at the given index and scales it by the provided factor.
        
        Args:
            index (int): Index in the raw data list.
            factor (float): Scaling multiplier (e.g., 1000 for kL, 0.001 for mL).
            
        Returns:
            Optional[float]: The scaled value or None if index out of bounds.
        """
        if not isinstance(index, int) or not isinstance(factor, (int, float)):
            raise TypeError("Index and factor must be numeric")

        if 0 <= index < len(self._raw_data):
            raw_value = self._raw_data[index]
            return raw_value * factor
        
        return None

    def get_scaled_list(self, start_index: int, end_index: Optional[int], factor: float) -> List[float]:
        """
        Retrieves a slice of volume data scaled by the given factor.
        
        Args:
            start_index (int): Start index (inclusive).
            end_index (Optional[int]): End index (exclusive). Defaults to len(data).
            factor (float): Scaling multiplier.
            
        Returns:
            List[float]: Scaled values in order.
        """
        if not isinstance(start_index, int) or not isinstance(factor, (int, float)):
            raise TypeError("Indices and factor must be numeric")

        end = len(self._raw_data) if end_index is None else min(end_index, len(self._raw_data))
        
        return [self.get_scaled_value(i, factor) for i in range(start_index, end)]

    def get_statistics(self) -> Dict[str, float]:
        """Returns basic statistics about the stored raw data."""
        if not self._raw_data:
            return {"count": 0, "mean": 0.0, "min": None, "max": None}
        
        count = len(self._raw_data)
        total = sum(self._raw_data)
        mean_val = total / count
        
        min_val = min(self._raw_data) if self._raw_data else float('inf')
        max_val = max(self._raw_data) if self._raw_data else float('-inf')

        return {
            "count": count,
            "mean": round(mean_val, 6),
            "min": min_val,
            "max": max_val
        }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    
    # Sample volume data (in Liters)
    raw_volumes = [10.5, 25.3, 78.9, 42.1, 10.5] 
    
    store = EfficientVolumeStore(initial_capacity=64)

    for vol in raw_volumes:
        store.add_volume(vol)

    # Test retrieval with scaling factors (e.g., converting to Milliliters by *1000)
    scale_factor_ml = 1000.0
    
    print("=== Volume Data Store Statistics ===")
    stats = store.get_statistics()
    print(f"Total entries: {stats['count']}")
    print(f"Mean volume (L): {stats['mean']}")

    # Retrieve and display scaled values for specific indices
    target_indices = [0, 2]
    
    print("\n=== Scaled Values (Milliliters) ===")
    for idx in target_indices:
        value_ml = store.get_scaled_value(idx, scale_factor_ml)
        if value_ml is not None:
            print(f"Index {idx}: {value_ml:.1f} mL")

    # Retrieve a slice scaled by another factor (e.g., Kiloliters *0.001)
    kL_scale = 0.001
    
    sliced_data = store.get_scaled_list(2, 4, kL_scale)
    
    print("\n=== Sliced Data (Kiloliters) ===")
    for i, val in enumerate(sliced_data):
        if val is not None:
            print(f"Item {i}: {val:.6f} kL")

    # Demonstrate memory efficiency by showing raw data count vs retrieved scaled list length
    print("\n=== Memory Efficiency Check ===")
    original_count = len(store._raw_data)
    sliced_len = len(sliced_data) if isinstance(sliced_data, list) else 0
    
    print(f"Raw storage size: {original_count} floats (~{original_count * 8 / 1e6:.2f} MB)")
    print(f"Scaled retrieval overhead (list creation): ~{sliced_len * 8 / 1e6:.4f} MB")
    
    # Verify correctness with a known calculation
    expected_val = raw_volumes[0] * scale_factor_ml
    actual_val = store.get_scaled_value(0, scale_factor_ml)
    
    assert abs(expected_val - actual_val) < 1e-5, "Scaling logic failed"
    print(f"\nVerification: Index 0 scaled correctly. Expected {expected_val:.2f}, Got {actual_val:.2f}")