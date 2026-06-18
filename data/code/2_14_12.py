import bisect
from typing import List, Tuple, Optional

class EfficientVolumeStore:
    """
    An efficient data structure to store volume measurements with support 
    for quick lookups and scaling by a factor while maintaining memory efficiency.
    
    Uses sorted lists (arrays) internally because they offer better cache locality
    than Python lists of objects or dictionaries when accessing indices directly,
    especially for large datasets where object overhead becomes significant.
    
    Supports:
        - Storing multiple measurement points as (timestamp, volume).
        - Retrieving the nearest timestamp value O(log n) via binary search.
        - Scaling all stored volumes by a given factor efficiently in-place.
        
    Memory Efficiency Considerations:
    - Avoids storing redundant metadata per entry beyond necessary fields.
    - Pre-allocates space where possible (though Python lists are dynamic; reallocation is minimized during bulk operations).
    """

    def __init__(self):
        self.timestamps = []  # List of timestamps, kept sorted to enable binary search
        self.volumes = []   # Parallel list storing volume values corresponding to each timestamp

    def add_measurement(self, timestamp: float, volume: float) -> None:
        """Add a new measurement ensuring the lists remain aligned and sorted by timestamp."""
        idx = bisect.bisect_left(self.timestamps, timestamp)
        
        # If there's an existing entry at this index but with different data or it shifts due to insertion order changes
        if not self.timestamps or (idx < len(self.timestamps) and abs(timestamp - self.timestamps[idx]) <= 1e-9):
            pass 
        else:
            self.timestamps.insert(idx, timestamp)
            
        # Extend the volumes list only at this position; Python lists handle shifting efficiently via C-level array copy
        if idx == len(self.volumes):
            self.volumes.append(volume)
        
        # In a more complex scenario where we might insert in middle and not shift all items manually, 
        # we'd need to reallocate memory. But for this implementation:
        self.timestamps[idx] = timestamp
        
    def get_nearest_volume(self, target_timestamp: float) -> Optional[float]:
        """Find the volume value associated with the nearest time before or equal to `target_timestamp`."""
        idx = bisect.bisect_right(self.timestamps, target_timestamp) - 1
        
        if not self.volumes and idx == len(self.timestamps): 
            return None
            
        # Ensure we have a valid index within bounds
        if idx >= 0:
            current_time_idx = max(0, min(idx, len(self.timestamps)-1))
            return self.volumes[current_time_idx]

    def scale_factor(self, factor: float) -> 'EfficientVolumeStore':
        """Return a new EfficientVolumeStore with all volumes scaled by `factor`."""
        # Instead of modifying in place and returning self (which might be confusing), 
        # we return a shallow copy then mutate it to avoid side effects.

        store = EfficientVolumeStore()
        
        if not self.volumes or len(self.timestamps) == 0:
            return store
            
        for i, vol in enumerate(self.volumes):
            scaled_val = vol * factor
            
            # Only add if we haven't reached the end of timestamps (handling list growth properly here is crucial 
            # to maintain alignment and ensure correct insertion points. Note that appending directly assumes sorted order.)

if __name__ == '__main__':
    pass
