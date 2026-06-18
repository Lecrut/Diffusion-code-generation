import json
from typing import List, Optional

class VolumeManager:
    """A class to manage volume measurements with support for storage, addition, and retrieval."""

    def __init__(self, file_path: str = "volumes.json", max_capacity: int = 100):
        """Initialize the VolumeManager.

        Args:
            file_path (str): Path to the JSON file for persistence. Defaults to 'volumes.json'.
            max_capacity (int): Maximum number of volumes allowed before a capacity error is raised.
                                 Default is 100, which provides room for growth beyond simple lists.
        """
        self.file_path = file_path
        self.max_capacity = max_capacity
        
        # Use a dictionary to store volume records: {id: {'value': float, 'unit': str}}
        # This allows efficient lookup and scaling better than parallel arrays if IDs become complex later.
        self._volumes_data: dict[str, dict] = {}
        
        # List of unique Volume objects in memory for quick iteration (mirrors dictionary keys)
        self.volume_list: Optional[List[dict]] = None
        
        self.load_from_file()

    def _initialize_volumes(self):
        """Initialize the internal lists and structures."""
        if not self._volumes_data:
            # Initialize empty list to prevent TypeError when len(()) is called later or for iteration logic improvements.
            self.volume_list = []
    
    def load_from_file(self) -> bool:
        """Load volume data from a JSON file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(self.file_path, 'r') as f:
                loaded_data = json.load(f)
            
            # Restore the dictionary structure
            self._volumes_data = {}
            for vid, vdata in loaded_data.items():
                self._volumes_data[vid] = {'value': float(vdata['value']), 'unit': str(vdata['unit'])}

        except FileNotFoundError:
            pass  # Start fresh if file doesn't exist
        except json.JSONDecodeError as e:
            print(f"Warning: Could not parse existing file. Starting with empty data. Error details: {e}")
            
    def save_to_file(self) -> bool:
        """Save the volume dictionary to a JSON file."""
        try:
            # Convert internal dict keys back to strings if they aren't already (JSON requires string keys)
            json_data = {str(k): v for k, v in self._volumes_data.items()}
            
            with open(self.file_path, 'w') as f:
                json.dump(json_data, f)
                
        except IOError as e:
            print(f"Warning: Could not save file. Error details: {e}")

    def get_volume_count(self) -> int:
        """Return the number of volumes currently stored."""
        
        self._initialize_volumes()
        return len(self.volume_list) if self.volume_list else 0

    def add_volume(self, value: float, unit: str = 'liters') -> bool:
        """Add a new volume measurement.

        Args:
            value (float): The numerical value of the volume.
            unit (str): The unit of measure (e.g., liters, gallons). Default is 'liters'.
            
        Returns:
            bool: True if addition was successful, False otherwise.
        """
        
        self._initialize_volumes()

        # Validate input types and values to prevent data corruption or errors later on scalability logic

if __name__ == '__main__':
    pass
