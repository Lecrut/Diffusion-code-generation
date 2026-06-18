def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order.
    
    Uses Python's built-in Timsort algorithm via sorted() with reverse=True,
    which is highly optimized (O(n log n)) and stable for general-purpose sorting.

    Args:
        volumes (list[float|int]): A list containing numeric volume values.

    Returns:
        list[float|int]: A new list with the same elements in descending order.
    
    Note: The original input list is not modified to preserve data integrity unless explicitly needed elsewhere.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are required
    sample_volumes = [50.2, 100.7, 33.4, 89.1, 15.6, 200.0]

    sorted_volumes = sort_volume_measurements_descending(sample_volumes)

    print("Sorted volumes in descending order:")
    for vol in sorted_volumes:
        # Ensure consistent output formatting if necessary (e.g., removing trailing zeros from floats)
        formatted_vol = float(f"{vol:.1f}")  # Simple normalization to one decimal place as per input style
        print(formatted_vol)

    assert sample_volumes == [50.2, 100.7, 33.4, 89.1, 15.6, 200.0], "Sample data must remain unchanged."