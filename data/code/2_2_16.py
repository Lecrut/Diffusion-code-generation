import json
from typing import List, Optional

class VolumeManager:
    """
    A class to manage volume measurements with support for storage, addition, 
    and retrieval of data in a scalable manner using JSON serialization.
    """

    def __init__(self, file_path: str = "volumes.json"):
        self.file_path = file_path
        self.volumes: List[dict] = []
        # Load existing volumes if the file exists
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.volumes = data.get('volumes', [])
        except FileNotFoundError:
            pass

    def store(self, volume_id: str, value: float, unit: str = "ml") -> bool:
        """
        Stores a new volume measurement.
        
        Args:
            volume_id (str): Unique identifier for the volume entry.
            value (float): The numerical value of the volume.
            unit (str): Unit of measurement (default is 'ml').
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self.volumes.append({
                "id": volume_id,
                "value": float(value),
                "unit": str(unit)
            })
            with open(self.file_path, 'w') as f:
                json.dump({"volumes": self.volumes}, f)
            return True
        except Exception:
            return False

    def add(self, volume_id: Optional[str] = None, value: float = 0.0, unit: str = "ml") -> bool:
        """
        Adds a new measurement or updates an existing one if ID is provided.
        
        Args:
            volume_id (str): Identifier for the entry to update; otherwise creates new.
            value (float): Value to add/update.
            unit (str): Unit of measure.
            
        Returns:
            bool: True if operation succeeded, False otherwise.
        """
        # Normalize values and units before storing
        normalized_value = float(value)
        
        return self.store(volume_id or f"vol_{len(self.volumes)+1}", normalized_value, unit)

    def retrieve(self, volume_id: Optional[str] = None) -> List[dict]:
        """
        Retrieves all stored volumes. If a specific ID is provided, returns only that entry.
        
        Args:
            volume_id (str): Filter by this ID; if None, return all entries.
            
        Returns:
            list: A list of dictionary objects representing the retrieved volumes.
        """
        if volume_id:
            # Find specific volume
            for vol in self.volumes:
                if vol["id"] == str(volume_id):
                    return [vol]
            return []
        
        return self.volumes

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = VolumeManager()

    # Sample data 1: Initial store operations
    assert manager.store("V001", 50, "ml") is True
    assert manager.add(value=25.5) is True
    assert manager.add(volume_id="V003", value=75.8, unit="L") is True

    # Sample data 2: Retrieval operations
    all_volumes = manager.retrieve()
    specific_volume = manager.retrieve("V001")

    print(f"Total volumes stored: {len(all_volumes)}")
    
    if len(specific_volume) > 0:
        vol_data = specific_volume[0]
        print(f"Volume ID: {vol_data['id']}")
        print(f"Value: {vol_data['value']}, Unit: {vol_data['unit']}")

    # Sample data 3: Verify scalability by adding more entries in a loop
    for i in range(1, 6):
        manager.add(volume_id=f"S{i}", value=float(i * 10), unit="ml")
    
    final_count = len(manager.retrieve())
    print(f"Final total volume count after scaling: {final_count}")

    # Verify specific retrieval works correctly for a scaled entry
    retrieved_scaled = manager.retrieve("S3")
    assert len(retrieved_scaled) == 1, "Specific ID retrieval failed."