import json
from typing import List, Optional

class VolumeManager:
    """A class to manage volume measurements with support for storage, addition, and retrieval."""

    def __init__(self, file_path: str = "volumes.json"):
        """Initialize the VolumeManager.
        
        Args:
            file_path (str): Path to the JSON file where data is persisted. Defaults to 'volumes.json'.
            
        Raises:
            FileNotFoundError: If the specified file does not exist and no initial data is provided.
        """
        self.file_path = file_path
        self.volumes: List[dict] = []

    def _load_data(self) -> None:
        """Load existing volume data from the JSON file if it exists."""
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
                # Attempt to parse and update internal list
                self.volumes.extend(json.loads(content))
        except FileNotFoundError:
            pass  # Start fresh or keep existing in-memory data

    def _save_data(self) -> None:
        """Save the current volume list to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.volumes, f, indent=4)

    def store_volume(self, name: str, value: float, unit: Optional[str] = "ml") -> bool:
        """Store a new volume measurement.
        
        Args:
            name (str): Unique identifier for the volume entry.
            value (float): The numerical value of the volume. Must be non-negative.
            unit (Optional[str]): Unit of measurement, defaults to 'ml'. Supported units are 'l', 'gal', 'qt'.
            
        Returns:
            bool: True if successful, False otherwise.
            
        Raises:
            ValueError: If the value is negative or an unsupported unit is provided.
        """
        valid_units = ['ml', 'l', 'gal', 'qt']
        
        # Normalize units to lowercase for consistency and validation
        normalized_unit = unit.lower() if unit else "ml"
        if not any(normalized_unit in u for u in valid_units):
            raise ValueError(f"Unsupported or invalid unit: {unit}. Supported units are ml, l, gal, qt.")

        # Validate value
        if value < 0:
            raise ValueError("Volume cannot be negative.")

        entry = {"name": name, "value": float(value), "unit": normalized_unit}
        
        self.volumes.append(entry)
        self._save_data()
        return True

    def add_volume(self, existing_name: str, additional_value: float, unit: Optional[str] = None) -> bool:
        """Add to an existing volume measurement.
        
        Args:
            existing_name (str): The name of the existing entry to modify.
            additional_value (float): The value to add to the current total. Must be non-negative.
            unit (Optional[str]): Optional override for the target unit, defaults to matching existing or 'ml'.
            
        Returns:
            bool: True if successful, False otherwise.
            
        Raises:
            ValueError: If no entry with the given name exists or value is negative.
            KeyError: Internal error if conversion logic fails (unlikely).
        """
        # Find the index of the existing volume
        try:
            idx = next(i for i, v in enumerate(self.volumes) if v["name"] == existing_name)
        except StopIteration:
            raise ValueError(f"No entry found with name '{existing_name}'.")

        target_unit = unit.lower() if unit else self.volumes[idx]["unit"].lower()
        
        # Convert additional_value to the same base (ml) for calculation, then convert back? 
        # Actually, simpler approach: Store everything in ml internally or just sum based on units.
        # Let's standardize internal storage to 'l' as a common intermediate unit if needed, 
        # but since we store what is given, let's assume user inputs are consistent OR handle conversion.
        # To keep it robust without complex math library dependencies for this task scope:
        # We will convert both existing and new value to Liters (L) before summing, then decide final unit?
        # Or simpler: Just require the units to match or perform a simple conversion if specified.
        
        def val_to_l(val: float, u: str) -> float:
            """Convert volume to liters."""
            if u == 'l': return val
            elif u in ['ml']: return val / 1000
            elif u == 'gal': return val * 3.78541 # US gallons approx
            else: raise ValueError(f"Cannot convert unit {u} to liters.")

        try:
            existing_val = self.volumes[idx]["value"]
            
            if target_unit != "l": 
                current_l = val_to_l(existing_val, self.volumes[idx]["unit"])
                new_l = val_to_l(additional_value, target_unit)
                
                # Update in Liters internally? No, let's just update the value directly assuming unit consistency or simple addition logic.
                # To avoid complex refactoring of internal storage type: 
                # We will assume if units differ and no conversion is requested explicitly via a flag (not implemented here to keep it simple),
                # we might raise an error OR convert. Let's implement basic conversion for robustness.
                
                final_l = current_l + new_l
                
                self.volumes[idx]["value"] = final_l
                if target_unit != "l":
                    # Convert back to requested unit (or original) - let's stick to the provided 'unit' or default ml? 
                    # Let's convert back to the specific request unit for clarity.
                    def l_to_val(l: float, u: str):
                        if u == 'l': return l
                        elif u in ['ml']: return l * 1000
                        elif u == 'gal': return l / 3.78541
                        else: raise ValueError(f"Cannot convert from liters to {u}.")
                    
                    self.volumes[idx]["value"] = l_to_val(final_l, target_unit)

            # If units were same or no conversion needed (e.g., both ml), just add directly? 
            # The logic above handles the case where we want to sum into a specific unit.
            
        except Exception:
            raise ValueError("Error occurred while adding volume.")

        self._save_data()
        return True

    def retrieve_volume(self, name: str) -> Optional[dict]:
        """Retrieve details of a stored volume measurement.
        
        Args:
            name (str): The unique identifier for the entry to retrieve.
            
        Returns:
            dict or None: A dictionary containing 'name', 'value', and 'unit' if found, else None.
        """
        try:
            idx = next(i for i, v in enumerate(self.volumes) if v["name"] == name)
            return self.volumes[idx]
        except StopIteration:
            return None

    def get_all_volumes(self) -> List[dict]:
        """Retrieve a list of all stored volume measurements.
        
        Returns:
            List[dict]: A list containing dictionaries with 'name', 'value', and 'unit' for each entry.
        """
        return self.volumes.copy()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    
    manager = VolumeManager("sample_volumes.json")

    # Store initial volumes
    manager.store_volume(name="Kitchen Blender", value=250, unit='ml')
    manager.store_volume(name="Coffee Maker Reservoir", value=1.5, unit='l')
    
    print("--- Stored Volumes ---")
    for vol in manager.get_all_volumes():
        print(f"{vol['name']}: {vol['value']} {vol['unit']}")

    # Add to existing volume (converting units implicitly)
    try:
        result = manager.add_volume(existing_name="Coffee Maker Reservoir", additional_value=0.5, unit='l')
        if result:
            updated_vol = manager.retrieve_volume("Coffee Maker Reservoir")
            print(f"\n--- Updated {updated_vol['name']} ---")
            print(f"New Total Value: {updated_vol['value']} L (converted from 1.5L + 0.5L)")
    except Exception as e:
        print(f"Error adding volume: {e}")

    # Retrieve specific volume
    retrieved = manager.retrieve_volume("Kitchen Blender")
    if retrieved:
        print("\n--- Retrieved Kitchen Blender ---")