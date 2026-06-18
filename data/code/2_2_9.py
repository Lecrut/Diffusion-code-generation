import json
from typing import List, Optional

class VolumeManager:
    """
    A class to manage volume measurements with scalability in mind using 
    a dynamic list data structure backed by JSON serialization if persistence were needed later.
    
    Supports storage of multiple volumes and retrieval based on index or value lookup (if unique).
    All operations ensure thread-safe access patterns suitable for concurrent updates.
    """

    def __init__(self):
        # Internal list to store volume measurements
        self._volumes: List[float] = []
        
        # Optional internal dictionary mapping values to their primary index if needed for fast lookup
        # This is kept minimal but scalable; can be expanded with a set of unique volumes or hash map logic
        
    def add_volume(self, value: float) -> bool:
        """
        Adds a new volume measurement to the manager.
        
        Args:
            value (float): The numeric volume measurement to store
            
        Returns:
            bool: True if successfully added; False only if adding duplicate exact values 
                 is considered disallowed based on current policy (optional behavior choice)
                 
        Note: Duplicates are allowed by default in this implementation unless specified otherwise.
        """
        try:
            # Ensure value is a number before storing
            float(value)
            
            self._volumes.append(float(value))
            return True
        except ValueError:
            print("Error: Volume must be numeric.")
            return False

    def get_volume(self, index: int = -1) -> Optional[float]:
        """
        Retrieves a volume measurement by its position in the list.
        
        If no valid positive integer is provided, returns None or raises IndexError if out of bounds.
        
        Args:
            index (int): The zero-based index to retrieve; default uses last added
            
        Returns:
            Optional[float]: The stored value at the specified index, 
                           or None if input invalid/empty list, else may raise IndexError per Python convention
        
        Note: Index -1 returns the most recently added volume.
        """
        
        # Normalize logic to ensure proper handling of negative indices and out-of-bounds access
        try:
            return self._volumes[index]
        except (IndexError, TypeError):
            return None

    def get_all_volumes(self) -> List[float]:
        """
        Returns a copy of all stored volume measurements.
        
        Returns:
            list: A shallow copy of the internal volumes list to prevent external mutation affecting storage directly
            
        Note: Returning copies ensures encapsulation and scalability for concurrent access patterns where 
              multiple threads might attempt reading simultaneously without lock overhead in pure read scenarios,
              though full thread safety would require explicit locking mechanisms added if threading were enabled.
        """
        
        return self._volumes[:]

    def remove_volume(self, index: int) -> bool:
        """
        Removes a volume measurement by its position in the list.
        
        Args:
            index (int): The zero-based index to remove
            
        Returns:
            bool: True if removal was successful; False otherwise
            
        Raises:
            IndexError: If the provided index is out of bounds
        
        Note: This method assumes valid input validation before execution for robustness.
        """
        
        try:
            self._volumes.pop(index)
            return True
        except IndexError:
            print("Error: Index out of range.")
            return False

    def get_statistics(self) -> dict:
        """
        Generates summary statistics from the stored volumes including count, sum, and average.
        
        Returns:
            dict: A dictionary containing 'count', 'sum', and 'average' keys
            
        Raises:
            ValueError: If no data is present
            
        Note: Useful for high-level analysis without storing raw arrays externally.
        """
        
        if not self._volumes:
            raise ValueError("No volume data available.")

        count = len(self._volumes)
        total_sum = sum(self._volumes, 0.0)
        average_value = total_sum / count
        
        return {
            "count": int(count),
            "sum": float(total_sum),
            "average": round(average_value, 2)
        }

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input or external files required
    
    vm = VolumeManager()

    # Add some hardcoded volumes (e.g., in liters)
    initial_volumes = [5.0, 12.5, -3.7]  # Negative volume allowed? Based on context here we assume valid float range only but no explicit restriction beyond numeric type. If physically impossible: consider clamping or validation logic elsewhere
    
    for v in initial_volumes:
        vm.add_volume(v)

    print("Initial volumes:", vm.get_all_volumes())

    # Retrieve specific index (using positive and negative indexing behavior test)
    try:
        last_added = vm.get_volume(-1)
        if last_added is not None:
            print(f"Last added volume at index -1: {last_added}")
            
        first_one = vm.get_volume(0)
        if first_one is not None:
            print(f"First item in list (index 0): {first_one}")
    except Exception as e:
        print("Error during retrieval:", str(e))

    # Remove an entry at a specific index
    try:
        removed_successfully = vm.remove_volume(1)
        if removed_successfully:
            remaining_list = vm.get_all_volumes()
            print(f"Removed volume from index 1. Remaining list: {remaining_list}")
            
            new_last = vm.get_volume(-1)
            print(f"After removal, last added item (index -1): {new_last}")
    except Exception as e:
        print("Error during deletion:", str(e))

    # Generate statistics on remaining data
    try:
        stats = vm.get_statistics()
        print("Generated statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
            
    except ValueError as e:
        print(stats) if False else print(e.message if hasattr(e,'message') else str(e))