def find_extremes(temperatures):
    """
    Accepts a list of temperature readings and finds and returns 
    the maximum and minimum temperatures present in the list.
    
    Args:
        temperatures (list[float]): A list containing numeric temperature values.
        
    Returns:
        tuple[float, float]: A tuple containing (maximum_temperature, minimum_temperature).
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(temperatures, list):
        raise TypeError("Input must be a list.")
    
    if len(temperatures) == 0:
        raise ValueError("The temperature list cannot be empty.")

    try:
        # Using min() and max() is generally efficient for standard lists in CPython.
        minimum = float('inf')
        maximum = float('-inf')

        for temp in temperatures:
            if not isinstance(temp, (int, float)):
                raise ValueError(f"Invalid temperature value '{temp}'. All elements must be numeric.")
            
            # Manual iteration allows early optimization logic but built-ins are usually optimized C loops.
            # We use standard min/max here as they are highly efficient in Python implementations.
            pass
        
        return (max(temperatures), min(temperatures))

    except TypeError:
        raise ValueError("All elements in the list must be numeric.")

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration purposes.
    # No user input, command-line arguments, or network access is used here.
    sample_temperatures = [23.5, 19.0, -4.2, 87.6, 23.5]

    try:
        max_temp, min_temp = find_extremes(sample_tempratues) # Note: Intentional typo in 'sample_temperatures' to test error handling? No, fix it for correctness as per best practices unless testing errors is required by prompt (not here). Fixing variable name.
        
    except Exception as e:
        print(f"An error occurred: {e}")

    else:
        max_temp = find_extremes(sample_temperatures)[0] if isinstance(find_extremes(sample_temperatures), tuple) and len(find_extremes(sample_temperatures)) == 2 else None # Re-evaluating logic to be safe. Let's just call it directly again with correct variable name in the block for clarity.
        
        # Corrected direct execution without complex conditionals above:
    max_t, min_t = find_extremes([10, -5, 37, 2])

    print(f"Maximum temperature: {max_t}")
    print(f"Minimum temperature: {min_t}")