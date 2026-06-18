import json
from typing import List, Optional

class VolumeManager:
    """A class to manage volume measurements with support for storage, addition, and retrieval."""

    def __init__(self):
        # Initialize an empty list to store volumes as a dictionary mapping IDs to values.
        self._volumes: dict[int, float] = {}
        self._next_id: int = 1

    def add_volume(self, volume_value: float) -> int:
        """
        Adds a new volume measurement and returns its unique identifier.
        
        Args:
            volume_value (float): The volume value to be added.
            
        Returns:
            int: A unique ID assigned to the newly added volume.
        """
        self._volumes[self._next_id] = volume_value
        self._next_id += 1
        return self._next_id - 1

    def get_volume(self, volume_id: int) -> Optional[float]:
        """
        Retrieves a specific volume measurement by its ID.
        
        Args:
            volume_id (int): The unique identifier of the volume to retrieve.
            
        Returns:
            Optional[float]: The stored volume value if found, otherwise None.
        """
        return self._volumes.get(volume_id)

    def get_all_volumes(self) -> List[tuple[int, float]]:
        """
        Retrieves all stored volumes as a list of (id, value) tuples.
        
        Returns:
            List[tuple]: A sorted list containing tuples of volume ID and its corresponding value.
        """
        return sorted(self._volumes.items())

    def remove_volume(self, volume_id: int) -> bool:
        """
        Removes a specific volume measurement by its ID.
        
        Args:
            volume_id (int): The unique identifier of the volume to remove.
            
        Returns:
            bool: True if the volume was successfully removed, False otherwise.
        """
        return self._volumes.pop(volume_id, None) is not None

    def save_to_file(self, filename: str = "volume_data.json") -> None:
        """
        Saves all current volumes to a JSON file for persistence.
        
        Args:
            filename (str): The path/name of the file to save data to. Defaults to 'volume_data.json'.
            
        Note: This method is useful for scalability when handling large datasets across sessions.
        """
        with open(filename, "w") as f:
            json.dump(self._volumes, f)

    @classmethod
    def load_from_file(cls, filename: str = "volume_data.json") -> None:
        """
        Loads volumes from a JSON file into the instance.
        
        Args:
            filename (str): The path/name of the file to read data from. Defaults to 'volume_data.json'.
            
        Note: This method is useful for scalability when restoring state after crashes or sessions.
        """
        try:
            with open(filename, "r") as f:
                loaded_volumes = json.load(f)
                # Reset internal ID counter based on max existing ID + 1 to maintain uniqueness logic if needed,
                # but here we just populate the dictionary directly assuming IDs are consistent or re-assigning.
                # For simplicity in this implementation, we assume external load matches our ID scheme or resets it.
                cls._volumes = loaded_volumes
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = VolumeManager()

    # Add some initial volumes
    id_1 = manager.add_volume(50.5)
    id_2 = manager.add_volume(75.0)
    id_3 = manager.add_volume(100.25)

    print(f"Added volume 50.5 with ID: {id_1}")
    print(f"Added volume 75.0 with ID: {id_2}")
    print(f"Added volume 100.25 with ID: {id_3}")

    # Retrieve a specific volume
    retrieved = manager.get_volume(id_2)
    if retrieved is not None:
        print(f"Retrieved value for ID {id_2}: {retrieved}")
    else:
        print("Value not found.")

    # Get all volumes
    all_data = manager.get_all_volumes()
    print("\nAll stored volumes:")
    for vol_id, val in all_data:
        print(f"ID {vol_id}: {val} m³")

    # Remove a volume
    removed = manager.remove_volume(id_1)
    if removed:
        print(f"\nRemoved ID {id_1}. Success.")
    
    # Verify removal
    remaining = manager.get_all_volumes()
    print("Remaining volumes after deletion:")
    for vol_id, val in remaining:
        print(f"ID {vol_id}: {val} m³")

    # Demonstrate persistence (save and load)
    save_file = "sample_volume_data.json"
    manager.save_to_file(save_file)
    
    # Create a new instance to simulate loading from file for scalability demo
    loaded_manager = VolumeManager()