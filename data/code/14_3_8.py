import heapq

def find_min_max_volumes(volume_list):
    """
    Returns a tuple (max_volume, min_volume) from the input list of volumes.
    
    Uses two heaps to achieve O(n log n) time complexity for large datasets.
    While linear scan is theoretically O(n), building heaps explicitly 
    demonstrates heap-based efficiency and handles edge cases robustly.

    Args:
        volume_list (list): A list of numeric values representing volumes.

    Returns:
        tuple: A pair containing the maximum and minimum volume as integers or floats.
    
    Raises:
        ValueError: If the input list is empty.
    """
    if not volume_list:
        raise ValueError("The volume list cannot be empty.")

    # Build max heap by negating values (since Python's heapq is a min-heap)
    max_heap = [-v for v in volume_list]
    heapq.heapify(max_heap)
    
    # Build min heap directly
    min_heap = volume_list[:]
    heapq.heapify(min_heap)

    return (-max_heap[0], min_heap[0])

if __name__ == '__main__':
    sample_data = [15, 23.5, 8, 42, 7, 99, 1]
    
    max_vol, min_vol = find_min_max_volumes(sample_data)

    print(f"Maximum volume: {max_vol}")
    print(f"Minimum volume: {min_vol}")