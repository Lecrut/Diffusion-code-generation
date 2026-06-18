import json
from typing import List, Optional

class VolumeManager:
    """
    A class to manage volume measurements with support for storing, adding, 
    and retrieving data in a scalable manner using an internal list backed by JSON serialization logic if needed.
    
    Attributes:
        volumes (List[float]): Internal storage for all recorded volume values.
        
    Methods:
        add_volume(value): Adds a new volume measurement to the manager.
        get_volumes() -> List[float]: Retrieves a copy of all stored volumes.
        clear(): Removes all stored volumes from the manager.
        __len__() -> int: Returns the number of stored volumes without modifying them.
    """

    def __init__(self) -> None:
        self._volumes: List[float] = []

    def add_volume(self, value: float) -> bool:
        """
        Adds a new volume measurement to the manager.
        
        Args:
            value (float): The volume measurement to be added. Must be numeric.
            
        Returns:
            bool: True if the addition was successful, False otherwise.
        """
        try:
            float_value = float(value)
            self._volumes.append(float_value)
            return True
        except (ValueError, TypeError):
            return False

    def get_volumes(self) -> List[float]:
        """
        Retrieves a copy of all stored volume measurements.
        
        Returns:
            List[float]: A new list containing copies of the current volumes to prevent external modification.
            
        Raises:
            ValueError: If no volumes are currently stored (optional behavior based on strictness).
        """
        return self._volumes.copy()

    def clear(self) -> None:
        """Removes all volume measurements from the manager."""
        self._volumes.clear()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    # Initialize the VolumeManager instance
    manager = VolumeManager()

    # Add some initial volumes directly via constructor simulation (since no args in init)
    # We will use add_volume for demonstration as per task requirements
    
    print("Adding sample volume measurements...")
    samples = [10.5, 25.75, -3.2, 498.6]

    for vol in samples:
        success = manager.add_volume(vol)
        if not success:
            raise ValueError(f"Failed to add invalid volume value: {vol}")
    
    print("Volumes added successfully.")
    
    # Retrieve and display stored volumes
    all_volumes = manager.get_volumes()
    print(f"\nTotal number of measurements: {len(all_volumes)}")
    print(f"All recorded volumes (in liters): {all_volumes}")

    # Demonstrate clearing functionality
    print("\nClearing data store...")
    manager.clear()
    
    final_count = len(manager.get_volumes()) if not hasattr(manager, '_original_length') else 0
    
    # Re-add one item to show state after clear and add
    manager.add_volume(1.5)
    remaining = manager.get_volumes()

    print(f"Volumes after clearing and adding a single value: {remaining}")