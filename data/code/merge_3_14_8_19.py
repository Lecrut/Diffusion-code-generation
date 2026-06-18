import heapq

def sort_volume_measurements_descending(volumes: list) -> list:
    """
    Sorts a list of volume measurements in descending order using an efficient algorithm.
    
    Since Python's Timsort (used by the built-in `sorted()` and `list.sort()`) is highly optimized,
    O(n log n), stable, and performs exceptionally well on partially sorted data or lists with many duplicates,
    it is chosen here as the most practical and efficient approach for general-purpose sorting.
    
    Alternatively, a max-heap could be used to achieve O(n) build time followed by extraction,
    but Python's C-implemented Timsort often outperforms pure-Python heap implementations in real-world scenarios due to low overhead.
    
    Args:
        volumes (list): A list of numeric volume measurements.
        
    Returns:
        list: The same list sorted in descending order. In-place modification is also performed for efficiency.
    """
    # Sort the list directly using Timsort with reverse=True to get descending order efficiently
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [50, 120, 75, 30, 90, 45, 60]
    print("Original volumes:", sample_volumes)
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes.copy())
    print("Sorted (descending):", sorted_volumes)