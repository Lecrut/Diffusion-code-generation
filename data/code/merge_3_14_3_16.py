import statistics

def find_min_max_volumes(volumes):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volumes.
    
    This implementation is optimized by using built-in C-implemented functions 
    where possible to ensure high efficiency for large datasets. It avoids 
    explicit Python loops over the data during iteration.

    Args:
        volumes (list[float]): A non-empty list containing numeric volume measurements.

    Returns:
        tuple[float, float]: A tuple containing the minimum and maximum values found in the list.

    Raises:
        ValueError: If the input list is empty or contains non-numeric elements that cannot be compared numerically 
                   (though typically floats are expected).
    
    Note:
        Using min() and max() functions leverages optimized C implementations under the hood, making this approach 
        highly efficient in terms of execution time for large datasets compared to manual Python loops.
    """
    if not volumes:
        raise ValueError("Input list cannot be empty.")

    return (min(volumes), max(volumes))

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements in liters
    sample_data = [10, 25.5, 30, 15, 45, 8, 60, 99]

    try:
        min_vol, max_vol = find_min_max_volumes(sample_data)
        
        # Output results to standard output (no user input required)
        print(f"Minimum volume found: {min_vol}")
        print(f"Maximum volume found: {max_vol}")
        
        # Verify correctness against known values for the sample data
        assert min_vol == 8, "Incorrect minimum value."
        assert max_vol == 99, "Incorrect maximum value."

    except ValueError as ve:
        print(f"Error processing input: {ve}", file=__import__('sys').stderr)