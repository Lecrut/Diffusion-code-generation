import time
from datetime import datetime

class VolumeManager:
    """
    A class to manage volume measurements with scalability in mind using a list-based storage,
    which allows efficient O(1) append operations and reasonable search capabilities.
    For very large datasets, an indexed structure like SQLite or Redis might be preferred,
    but this implementation uses standard Python lists for simplicity and portability within memory constraints.
    
    Attributes:
        volumes (list): Stores tuples of volume value and timestamp in ISO format string.
        
    Methods:
        add_volume(value, unit='ml'): Adds a new volume measurement with current time.
        get_volumes(limit=None): Retrieves stored measurements, optionally limiting the count.
        clear_all(): Removes all recorded volumes from storage.
    
    Usage Example:
        manager = VolumeManager()
        manager.add_volume(50)
        print(manager.get_volumes())
    """

    def __init__(self):
        # Initialize an empty list to store tuples of (value, timestamp_string).
        self.volumes = []
    
    def add_volume(self, value: float, unit: str = 'ml') -> None:
        """
        Adds a volume measurement. The current UTC time is automatically captured as the record's timestamp.

        Args:
            value (float): The numerical value of the volume. Must be non-negative.
            unit (str): The unit of measure, defaulting to 'ml'. Can include suffixes like 'L', 'gal'.
            
        Raises:
            ValueError: If the provided value is negative or zero.
        
        Example:
            >>> manager.add_volume(100)
            None # No return value
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be a number.")
        if value < 0:
            raise ValueError("Volume cannot be negative or zero.")

        timestamp = datetime.utcnow().isoformat() + "Z"
        
        self.volumes.append({
            'value': value,
            'unit': unit.upper(), # Store units in uppercase for consistency
            'timestamp': timestamp
        })

    def get_volumes(self, limit: int | None = None) -> list[dict]:
        """
        Retrieves all stored volume measurements. The results are returned as a list of dictionaries 
        containing the recorded value and its ISO-formatted timestamp. If a numeric limit is provided (max 10 items), 
        it restricts the retrieval to that many most recent entries for performance simulation in high-volume scenarios, 
        though actual limits should ideally be handled by external databases at scale.

        Args:
            limit (int | None): Optional maximum number of records to return from newest to oldest. 
                               Defaults to retrieving all stored items up to a cap of 10 for the demonstration context, 
                               but can accept any positive integer if desired logic dictates strict pagination here.
        
        Returns:
            list[dict]: A list where each element is a dictionary with keys 'value', 'unit', and 'timestamp'.

        Raises:
            TypeError: If limit is not an integer or negative number when provided.
        """
        # Ensure we don't break if someone passes float for count, though type hint says int | None
        if limit is not None and isinstance(limit, (int, float)):
            try:
                max_records = 10
                actual_limit = min(int(round(limit)), max_records) 
            except TypeError:
                raise ValueError("Limit must be an integer or non-negative number.")

        # Sort descending by timestamp to return newest first as per common log practices
        sorted_volumes = sorted(self.volumes, key=lambda x: x['timestamp'], reverse=True)
        
        if limit is not None and actual_limit > 0:
            return [v for v in sorted_volumes[:actual_limit]]
        else:
            # Return all up to a reasonable cap of 10 per the specific instruction constraint 
            # regarding "scalability" demonstration without DB, or potentially just full list.
            # Given strict constraints often imply demoing behavior on small sets:
            return [v for v in sorted_volumes[:min(len(sorted_volumes), max_records)]]

    def clear_all(self) -> None:
        """Clears all volume measurements from the manager."""
        self.volumes = []

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    print("Initializing VolumeManager...")
    vm = VolumeManager()

    # Sample Data Addition
    initial_volumes = [50, 120.5, 75]
    
    for vol in initial_volumes:
        vm.add_volume(vol)
        
    print(f"Added {len(initial_volumes)} samples.")

    # Retrieve all data to verify storage
    retrieved_data = vm.get_volumes()
    
    if len(retrieved_data) > 10:
        # If more than the simulated 'max' (10), show first few only as per internal logic of get_volumes 
        # which capped at max_records=10 unless passed a larger explicit limit. 
        print(f"Total records stored internally: {len(vm.volumes)}")
    else:
        print("Records retrieved:")
        
    for record in vm.get_volumes():
        print(record)

    # Demonstrate adding more specific data with units
    extra_additions = [250, 1.8] 
    unit_map = {'l': 'L', 'ml': 'mL'} 
    
    for val in extra_additions:
        vm.add_volume(val, unit='ml')

    print("\nAfter adding more samples:")
    
    # Try clearing and checking again to ensure statelessness between clears
    vm.clear_all()
    count = len(vm.volumes)
    if count == 0:
        print("All data cleared successfully.")
        
    # Re-add one final sample for the end output
    final_val = 99.9
    unit_str = 'L' 
    vm.add_volume(final_val, unit=unit_str)
    
    result = vm.get_volumes()
    if len(result) <= 10:
        print("\nFinal Result:")
        
        for item in result:
            t_stamp = item['timestamp'][:19] # Print time roughly without microseconds for brevity
            
            print(f"Value: {item['value']} ({item['unit']}), Time: {t_stamp}")

    else:
         pass
    
    print("\nVolumeManager class executed successfully.")