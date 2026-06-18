import json
from typing import List, Optional

class VolumeManager:
    """
    A class to manage volume measurements with support for storage, addition, 
    and retrieval of data in a scalable manner using JSON serialization.
    
    Attributes:
        volumes (List[float]): Internal list storing all recorded volume values.
        file_path (str): Path to the persistent storage file (initialized by default).
        
    Methods:
        add_volume(value: float) -> None: Adds a new volume measurement.
        get_volumes() -> List[float]: Retrieves all stored volumes.
        save_to_file(file_path: str, data: dict) -> bool: Persists data to JSON file.
        load_from_file(file_path: str) -> Optional[dict]: Loads data from JSON file.
    """

    def __init__(self, initial_volumes: List[float] = None):
        """Initialize the VolumeManager with optional pre-loaded volumes."""
        self.volumes: List[float] = [] if initial_volumes is None else list(initial_volumes)

    def add_volume(self, value: float) -> bool:
        """
        Adds a new volume measurement to the internal storage.
        
        Args:
            value (float): The volume measurement to be added. Must be non-negative.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            if not isinstance(value, (int, float)):
                raise ValueError("Volume must be a number.")
            if value < 0:
                return False
            
            self.volumes.append(float(value))
            # Sort to maintain chronological order of addition for consistent retrieval
            self.sort_volumes()
            return True
        except Exception as e:
            print(f"Error adding volume: {e}")
            return False

    def get_volumes(self) -> List[float]:
        """Returns a copy of the list containing all stored volumes."""
        return list(self.volumes)

    def sort_volumes(self):
        """Sorts the internal volume list in ascending order for efficient retrieval and display."""
        self.volumes.sort()

    def save_to_file(self, file_path: str, data: dict = None) -> bool:
        """
        Persists the current state of volumes to a JSON file.
        
        Args:
            file_path (str): The path where the JSON data will be saved.
            data (dict, optional): Custom dictionary containing additional metadata if needed. Defaults to empty dict with 'volumes' key.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            output = {'volumes': self.volumes}
            if data is not None and isinstance(data, dict):
                output.update(data)
            
            with open(file_path, 'w') as f:
                json.dump(output, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, file_path: str) -> Optional[dict]:
        """
        Loads volume data from a JSON file.
        
        Args:
            file_path (str): The path of the JSON file containing the data.
            
        Returns:
            dict or None: A dictionary with 'volumes' key if successful, otherwise None.
        """
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"Error loading from file: {e}")
            return None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access
    
    # Create a VolumeManager instance with initial volumes
    manager = VolumeManager(initial_volumes=[10.5, 20.3, 15.7])

    print("Initial Volumes:", manager.get_volumes())

    # Add new volume measurements programmatically
    sample_values = [5.2, -3.4, 8.9] 
    
    for val in sample_values:
        result = manager.add_volume(val)
        status = "Added" if result else "Failed (invalid value)"
        print(f"Tried to add {val}: {status}")

    # Retrieve updated volumes after additions and sorting
    current_volumes = manager.get_volumes()
    print("\nUpdated Volumes:", current_volumes)

    # Demonstrate file persistence with a temporary path constructed from hardcoded string
    temp_file_path = "temp_volume_data.json"
    
    # Save the data to a JSON file (simulating external storage management)
    manager.save_to_file(temp_file_path, {'timestamp': '2023-10-27T10:00:00'})
    print(f"\nData saved to {temp_file_path}")

    # Simulate loading data back into a new instance (demonstrating scalability via file I/O)
    loaded_data = manager.load_from_file(temp_file_path)
    
    if loaded_data is not None and 'volumes' in loaded_data:
        print("Loaded Volumes from File:", loaded_data['volumes'])

    # Clean up temporary file to ensure no pre-existing files remain after execution
    import os
    try:
        os.remove(temp_file_path)
        print(f"\nTemporary file {temp_file_path} removed.")
    except FileNotFoundError:
        pass  # File might not exist if save failed or was already gone