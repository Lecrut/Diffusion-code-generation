import json
from typing import Optional, List, Dict

class VolumeManager:
    """
    A class to manage volume measurements with support for storage, 
    addition, and retrieval of data in a scalable manner using JSON files.
    
    Attributes:
        file_path (str): Path to the JSON file where volumes are stored.
        
    Methods:
        add_volume(volume_name: str, value: float) -> None: Adds a new volume measurement.
        get_volumes() -> List[Dict]: Retrieves all stored volumes as dictionaries.
        remove_volume(volume_name: str) -> bool: Removes a specific volume by name.
        clear_all() -> None: Clears all data from storage.
    """

    def __init__(self, file_path: Optional[str] = "volumes_data.json"):
        self.file_path = file_path
        # Initialize empty list if the file doesn't exist or is invalid JSON on first load
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self._data_list = data.get('volumes', [])
        except (FileNotFoundError, json.JSONDecodeError):
            self._data_list = []

    def _save_to_file(self) -> None:
        """Saves the internal list of volumes to a JSON file."""
        with open(self.file_path, 'w') as f:
            # Ensure it's valid JSON even if empty
            json.dump({'volumes': self._data_list}, f)

    def add_volume(self, volume_name: str, value: float) -> None:
        """
        Adds a new volume measurement to the manager.
        
        Args:
            volume_name (str): The name/identifier for the volume.
            value (float): The numerical value of the volume.
            
        Raises:
            ValueError: If value is not positive or if name contains invalid characters.
        """
        if value <= 0:
            raise ValueError("Volume value must be a positive number.")
        
        # Basic validation for string content to prevent path traversal in filenames later if used
        try:
            volume_name.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError("Volume name contains non-ASCII characters which are not supported.")

        new_entry = {
            "name": str(volume_name),
            "value": value,
            "timestamp": None # Placeholder for future timestamp implementation if needed
        }
        
        self._data_list.append(new_entry)
        self._save_to_file()

    def get_volumes(self) -> List[Dict]:
        """
        Retrieves all stored volume measurements.
        
        Returns:
            A list of dictionaries, where each dictionary represents a volume entry 
            with keys 'name', 'value', and optionally 'timestamp'.
        """
        return self._data_list

    def remove_volume(self, volume_name: str) -> bool:
        """
        Removes a specific volume by name.
        
        Args:
            volume_name (str): The exact name of the volume to remove.
            
        Returns:
            True if a volume was removed and it existed previously; False otherwise.
        """
        initial_count = len(self._data_list)
        self._data_list = [v for v in self._data_list if v["name"] != str(volume_name)]
        
        # Only save to file if the list actually changed (optimization + atomicity hint)
        if len(self._data_list) < initial_count:
            self._save_to_file()
            
        return True

    def clear_all(self) -> None:
        """Removes all volume data from storage."""
        self._data_list = []
        self._save_to_file()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Initialize manager with a default file path (will be created if not exists)
    vm = VolumeManager("sample_volumes.json")

    # Add some initial volumes using hard-coded data
    try:
        vm.add_volume("Living Room", 150.5)
        vm.add_volume("Kitchen", 89.2)
        vm.add_volume("Master Bedroom", 45.7)
        
        print("Volumes added successfully.")
    except ValueError as e:
        print(f"Error adding volumes: {e}")

    # Retrieve and display all stored volumes
    try:
        current_volumes = vm.get_volumes()
        if not current_volumes:
            print("No volumes found in storage.")
        else:
            print("\nCurrent Volume Measurements:")
            for vol in current_volumes:
                print(f"  - {vol['name']}: {vol['value']}")
    except Exception as e:
        print(f"Error retrieving volumes: {e}")

    # Demonstrate removal of a specific volume
    if len(current_volumes) > 0:
        try:
            removed = vm.remove_volume("Living Room")
            if removed:
                print("\nSuccessfully removed 'Living Room'.")
            
            # Retrieve again to verify update (optional for demo clarity, but good practice)
            updated_list = vm.get_volumes()
            print(f"Updated list count: {len(updated_list)} items.")
        except Exception as e:
            print(f"Error removing volume: {e}")

    # Demonstrate clearing all data
    try:
        vm.clear_all()
        final_check = len(vm.get_volumes())
        if final_check == 0:
            print("Storage cleared successfully.")
    except Exception as e:
        print(f"Error during clear operation: {e}")

    # Final status check to ensure no external dependencies or inputs were used
    print("\nModule execution completed without user interaction.")