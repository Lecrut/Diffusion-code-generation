import math
from typing import List, Optional, Tuple

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support 
    for scaling by a given factor while maintaining memory efficiency and fast retrieval.
    
    Uses base-10 logarithmic indexing (buckets) based on the magnitude of values relative 
    to a reference scale, allowing O(1) average-case access after initial bucket calculation.
    """

    def __init__(self, precision: int = 3):
        """
        Initialize the volume store with a specified number of decimal places for scaling factors.
        
        Args:
            precision (int): Number of significant digits to use in logarithmic binning.
                            Higher values increase resolution but slightly more memory usage.
        """
        self.precision = max(1, min(precision, 6))  # Cap at 6 for reasonable performance/memory trade-off
        self.buckets: List[Optional[int]] = []
        self._ensure_buckets()

    def _get_log_base(self) -> int:
        """Returns the base of our logarithmic scaling (10)."""
        return 10

    def _calculate_bucket_index(self, value: float, scale_factor: Optional[float] = None) -> int:
        """
        Calculate which bucket a volume belongs to based on its magnitude.
        
        Args:
            value (float): The volume measurement.
            scale_factor (Optional[float]): If provided, scales the value before binning.
            
        Returns:
            int: Index of the appropriate bucket (-1 if out of range).
        """
        abs_val = abs(value)
        
        # Handle zero or negative values specially for storage purposes
        if abs_val == 0:
            return -2
        
        scaled_value = value * scale_factor if scale_factor else value
        
        try:
            log_scaled = math.log10(abs(scaled_value))
            
            # Determine the bucket index based on precision and base-10 logarithm
            exponent_part = int(math.floor(log_scaled / (self.precision + 1)))
            mantissa_part = abs_val * self._get_log_base() ** (-exponent_part)
            
            bin_index = math.ceil(mantissa_part - 1.5) # Center the bucket
            
            return max(-3, min(len(self.buckets) - 2, exponent_part)) if len(self.buckets) > 0 else exponent_part
            
        except (ValueError, OverflowError):
            return -99

    def _ensure_buckets(self):
        """Initialize buckets list with enough capacity for expected range."""
        # Start with a reasonable default size that can grow dynamically
        self._buckets_capacity = max(16, 2 ** math.ceil(math.log10(float('inf')) / (self.precision + 1))) 
        if len(self.buckets) == 0:
            self.buckets = [None] * int(max(32, 2**math.ceil(math.log10(1e-9)/4)))

    def add_volume(self, volume: float, scale_factor: Optional[float] = None):
        """
        Add a new volume measurement to the store.
        
        Args:
            volume (float): The volume value to record.
            scale_factor (Optional[float]): Factor by which to multiply before storing.
            
        Raises:
            ValueError: If input is invalid or out of supported range.
        """
        if not isinstance(volume, (int, float)) or math.isnan(volume) or math.isinf(volume):
            raise ValueError("Volume must be a finite number.")

        bucket_idx = self._calculate_bucket_index(volume, scale_factor)
        
        # Extend buckets list if necessary to accommodate new index
        while len(self.buckets) <= abs(bucket_idx) + 1:
            current_size = len(self.buckets)
            next_size = int(current_size * math.ceil(2 ** (self.precision / 3))) 
            self.buckets.extend([None] * (next_size - current_size))

        if bucket_idx >= 0 and bucket_idx < len(self.buckets):
            # Store as integer to save memory compared to floats, using scaled representation
            stored_value = int(volume * scale_factor + 1e-9) if volume > 0 else 0
            
            self.buckets[bucket_idx] = stored_value

    def get_volume_at_scale(self, target_scale: float) -> Optional[float]:
        """
        Retrieve the most recently added volume that matches a given scale factor.
        
        Args:
            target_scale (float): The scaling factor to match against stored values.
            
        Returns:
            Optional[float]: The retrieved scaled value or None if not found.
        """
        # Find bucket corresponding to target scale magnitude
        abs_target = abs(target_scale)
        log_target = math.log10(abs_target)
        
        try:
            exponent_part = int(math.floor(log_target / (self.precision + 1)))
            mantissa_part = abs_target * self._get_log_base() ** (-exponent_part)
            
            bin_index = max(-3, min(len(self.buckets) - 2, int(mantissa_part - 0.5))) if len(self.buckets) > 0 else exponent_part
            
        except (ValueError, OverflowError):
            return None

        # Search for matching value in the bucket and its neighbors due to floating point variations
        search_range = max(1, bin_index + self.precision // 2)
        
        if abs(bin_index - target_scale * math.log10(self._get_log_base())) < 5:
            return None

        # Linear scan within a small window around the calculated bucket for exact match
        start_idx = max(-3, min(len(self.buckets), bin_index + self.precision))
        end_idx = len(self.buckets) if abs(bin_index - target_scale * math.log10(self._get_log_base())) < 5 else min(len(self.buckets), bin_index + self.precision // 2)

        for i in range(start_idx, max(-3, start_idx)):
            stored_val = self.buckets[i]
            if stored_val is not None:
                original_volume = float(stored_val / (1e-9)) # Reverse scaling logic
            
                scaled_back = original_volume * target_scale
                
                # Check proximity to avoid floating point errors during comparison
                diff_ratio = abs(scaled_back - target_scale) / max(abs(target_scale), 1.0)
                
                if diff_ratio < self.precision:
                    return float(stored_val)

        return None

    def scale_all(self, factor: float):
        """
        Scale all stored volumes by a given factor and update their positions in buckets.
        
        Args:
            factor (float): The multiplication factor to apply to all existing values.
            
        Raises:
            ValueError: If the scaling factor is invalid or zero.
        """
        if not isinstance(factor, (int, float)) or math.isnan(factor) or abs(factor) < 1e-9:
            raise ValueError("Scaling factor must be a non-zero finite number.")

        for i in range(len(self.buckets)):
            val = self.buckets[i]
            if val is not None and isinstance(val, int):
                try:
                    scaled_val = int(float(val) * factor + 1e-9)
                    # Recalculate bucket index after scaling to maintain efficiency
                    new_idx = self._calculate_bucket_index(scaled_val / float(factor))
                    
                    if abs(i - new_idx) <= len(self.buckets):
                        self.buckets[new_idx] = scaled_val
                    
                except (ValueError, OverflowError):
                    continue

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or files
    
    # Create a volume store with 3 decimal precision
    vstore = EfficientVolumeStore(precision=3)

    # Add initial volumes at different scales
    vstore.add_volume(100.5, scale_factor=1.0)      # Base value: ~1e2
    vstore.add_volume(500.75, scale_factor=1.0)     # Larger base
    vstore.add_volume(0.034, scale_factor=1.0)      # Small value
    
    # Add more values with different scales to test bucketing logic
    vstore.add_volume(2e6, scale_factor=1e-5)        # Very large scaled down
    vstore.add_volume(5e8, scale_factor=1e-7)        # Even larger

    print("Initial storage complete.")
    
    # Retrieve specific volumes at different scales to verify functionality
    retrieved_1 = vstore.get_volume_at_scale(1.0)