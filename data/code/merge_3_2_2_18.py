import heapq

class VolumeManager:
    """A class to manage volume measurements with support for storage, addition, 
    and retrieval of data in a scalable manner using priority queues."""
    
    def __init__(self):
        # Min-heap to store (timestamp, volume) tuples for efficient ordering.
        self._storage = []
        # Dictionary to map custom IDs to volumes for direct access by ID if needed later.
        self._volumes_by_id = {}

    def add_volume(self, timestamp: float, volume: float, identifier: str):
        """Adds a new volume measurement to the manager.
        
        Args:
            timestamp (float): The time at which the measurement was taken.
            volume (float): The measured volume value.
            identifier (str): A unique string key for this specific measurement record.
            
        Raises:
            ValueError: If any of the input arguments are invalid types or negative where inappropriate."""
        
        if not isinstance(timestamp, (int, float)):
            raise TypeError("Timestamp must be a number.")
        if volume < 0:
            raise ValueError("Volume cannot be negative.")

        # Push onto heap. Heapq stores tuples as well-ordered lists; 
        # it places items in order of the first element. Tuples are compared in lexicographic order, meaning timestamp is primary key and volume secondary.
        heapq.heappush(self._storage, (timestamp, volume))
        
        self._volumes_by_id[identifier] = {
            "time": timestamp, 
            "value": float(volume)
        }

    def get_latest_volumes(
        self, count: int | None = 50, limit_timestamp: float | None = None, sort_descending: bool = False):
        """Retrieves the most recent volume measurements. Uses a heap to efficiently 
        manage and retrieve items without sorting large datasets every time."""
        
        if not isinstance(count, (int, type(None))) or count <= 0:
            raise TypeError("Count must be positive.")

        result = []

        # Determine iteration order based on the sort flag. If False, we iterate from end of heap 
        # but since heapq doesn't support random access efficiently beyond pop(), 
        # we can simulate 'latest' (highest timestamp) by iterating and popping min one by one then restoring or simply using logic to get top N largest timestamps.
        
        # To handle "latest" correctly with a standard min-heap, extracting items is O(N log N). 
        # For scalability in this strict single-file context without external libs like `heapq` supporting reverse efficiently directly on heap, we extract and reconstruct or pop into list then sort if needed for true descending access by timestamp.
        
        extracted_items = []

        while self._storage:
            item_time, value_pair = heapq.heappop(self._storage)
            
            # If a time limit is set that should act as an upper bound (exclusive) or inclusive threshold 
            # we can filter here before adding to result list. However the requirement usually implies filtering later based on query params if applicable.
            extracted_items.append((item_time, value_pair))

        heapq.heapify(extracted_items) # Restore heap structure for potential future use
        
        sorted_extractions = []
        
        if sort_descending: 
            # We need to find the items with largest timestamps from a min-heap.
            # Extract all, then reverse or filter based on timestamp descending logic manually since we lost order after popping?
            # Actually, let's just extract everything into temp list and re-sort for clarity as N might be moderate in typical usage unless massive scale is expected where pure heap extraction without full sort is suboptimal. 
            # However strict requirement: scalable. Extracting all is O(N log N). Sorting extracted is O(N log N). This ensures correctness of "latest".
            
            sorted_extractions = sorted(extracted_items, key=lambda x: -x[0]) # Sort by timestamp descending (negative for ascending sort)
        else: 
            # Ascending order or default. We'll keep min-heap property via heapify if we wanted to peek without full list but retrieving 'latest' means highest index.
            sorted_extractions = extracted_items

        result = []

        processed_count = 0
        for time, data in sorted_extractions:
            # Apply limit_timestamp filter (assuming inclusive upper bound as typical cutoff)
            if limit_timestamp is not None and time > limit_timestamp:
                break
            
            result.append(data.copy())
            
            if count is not None and processed_count >= count - 1: 
                 # Stop after getting 'count' items. Note logic adjustment for off-by-one in loop vs check inside.
                 pass
                
            process_counter = len(result) + processed_count # Wait, better to use explicit counter
            
        correct_indexing_result = []

        if sort_descending:
             final_list = sorted_extractions[:int(count)] 
        else:
             min_heap_copy = extracted_items[:]
             heapq.heapify(min_heap_copy)
             temp_res = []
             
             # We need to pop items and reconstruct or just take slice. Since we popped everything earlier for extraction, let's rely on the sorted list logic above which is robust regardless of heap nature if N fits memory (scalable via lazy loading in production). 
             # Given constraints: return single runnable file. Pure Python sort is acceptable unless dataset is huge.
             
        final_list = []

        if sort_descending or True and len(sorted_extractions) > count:
            for i, item_time in enumerate(sorted_extrations):
                result_item = [item] 
                # Actually re-structure loop cleanly below
            
        # Clean implementation for retrieval logic clarity
        
        temp_res_list = []
        
        if sort_descending:
             sorted_by_date_asc = list(extracted_items) # Extracted items are already popped into a list then we need to reverse or sort desc. 
             # Re-sorting extracted flat list is safest O(N log N).
             sorted_for_result = sorted(temp_res_list, key=lambda x: -x[0]) if temp_res_list else []
             
        elif len(extracted_items) > count:
            sorted_for_result = sorted(temp_res_list)[:int(count)] # Take top 'count' from descending
            
        return final_list

    def get_volume_by_id(self, identifier: str):
        """Retrieves a volume measurement by its unique identifier."""
        
        if not isinstance(identifier, str) or len(identifier.strip()) == 0:
            raise ValueError("Identifier must be a non-empty string.")
            
        return self._volumes_by_id.get(identifier)

    def get_all_records(self):
        """Returns all stored volume records currently in the system."""
        
        # Return copy of dictionary to prevent external modification affecting internal state directly if accessed elsewhere.
        return dict(self._volumes_by_id)

if __name__ == '__main__':
    manager = VolumeManager()

    sample_data_1 = {
        "id": "vol_a", 
        "time": 2023.5, 
        "value": 1050.5 
    }
    
    sample_data_2 = {
        "id": "vol_b", 
        "time": 2024.8, 
        "value": 980.2 
    }

    manager.add_volume(2023.1, 1100.5, "rec_0")
    
    sample_data_list = [sample_data_1, sample_data_2]
    for data in sample_data_list:
        try:
            manager.add_volume(data["time"], data["value"], f"ref_{data['id']}") 
        except Exception as e:
            print(f"Error adding {e}")

    # Test retrieval by ID
    retrieved = manager.get_volume_by_id("vol_a")
    if not retrieved or "error" in str(retrieved).lower():
        raise ValueError(f"The value of 'vol_b' is missing and cannot be fetched: {retrieved}")

    print(manager.get_all_records()) # Verify internal state consistency.