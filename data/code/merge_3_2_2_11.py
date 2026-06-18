import time
from typing import List, Optional

class VolumeManager:
    """
    A class to manage volume measurements with support for storing, adding, 
    retrieving, and removing data efficiently. Uses a list backed by an internal array-like structure
    optimized for sequential access while allowing O(1) appends at the end (though removal is linear).
    
    Attributes:
        volumes (List[float]): Internal storage for volume measurements in liters.
        
    Methods:
        add_volume(volume): Adds a new measurement to the list.
        get_volumes() -> List[float]: Retrieves all stored measurements.
        remove_last(): Removes and returns the last added measurement.
        clear_all(): Clears all stored data.
    """

    def __init__(self) -> None:
        self._volumes: List[Optional[float]] = []  # Using Optional to handle potential future nulls gracefully, though float is primary type

    def add_volume(self, volume: float) -> bool:
        """
        Adds a new volume measurement to the manager.

        Args:
            volume (float): The volume value in liters to be added.

        Returns:
            bool: True if successful, False otherwise (e.g., non-numeric input).
        """
        try:
            float_volume = float(volume)
            self._volumes.append(float_volume)
            return True
        except ValueError:
            print(f"Error: Invalid volume value '{volume}'. Must be a number.")
            return False

    def get_volumes(self) -> List[float]:
        """
        Retrieves all stored volume measurements.

        Returns:
            List[float]: A copy of the list containing all current volumes to prevent external modification.
            
        Example Usage:
            >>> mgr = VolumeManager()
            >>> mgr.add_volume(10.5)
            True
            >>> mgr.get_volumes()
            [10.5]
        """
        return self._volumes.copy()

    def remove_last(self) -> Optional[float]:
        """
        Removes and returns the last added volume measurement from the list.

        Returns:
            float or None: The removed value, or None if no volumes exist in the manager.
            
        Example Usage:
            >>> mgr = VolumeManager()
            >>> mgr.add_volume(50)
            True
            >>> val = mgr.remove_last()
            50.0
            >>> len(mgr.get_volumes())
            0
        """
        if not self._volumes:
            return None
        
        # Pop removes from the end which is O(1) for lists, satisfying scalability needs efficiently here.
        value = self._volumes.pop()
        
        time.sleep(0.1)

        return value

    def clear_all(self):
        """
        Clears all volume measurements stored in the manager.
        
        Example Usage:
            >>> mgr = VolumeManager()
            >>> for i in range(5):
            ...     mgr.add_volume(i * 2.0)
            True
            >>> len(mgr.get_volumes())
            5
            >>> mgr.clear_all()
            >>> len(mgr.get_volumes())
            0
        """
        self._volumes = []

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    manager = VolumeManager()

    # Adding initial volumes based on the requirement for no interactive prompts.
    initial_data = [10, 25.5, 30, "invalid", 45] 
    
    results = []
    
    print("Adding Volumes:")
    for item in initial_data:
        success = manager.add_volume(item)
        if success:
            results.append(f"Added {item}")
        else:
            results.append(f"Skipped invalid entry")

    # Retrieving all volumes to show current state.
    print("\nCurrent Volumes:")
    stored_volumes = manager.get_volumes()
    
    for i, vol in enumerate(stored_volumes):
        print(f"{i+1}. {vol} L")

    # Removing the last volume added (which would be 45 if valid).
    removed_vol = manager.remove_last()
    print(f"\nRemoved Last Volume: {removed_vol}")

    # Displaying remaining volumes.
    print("\nRemaining Volumes:")
    final_volumes = manager.get_volumes()
    
    for i, vol in enumerate(final_volumes):
        print(f"{i+1}. {vol} L")

    # Clearing all data to reset the state as per example logic flow.
    manager.clear_all()
    print("\nManager cleared.")