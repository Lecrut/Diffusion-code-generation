def check_zeros(numbers):
    """
    Returns a list of booleans indicating whether each integer is zero.
    
    Parameters:
        numbers (list[int]): List of integers to evaluate.
        
    Returns:
        list[bool]: Boolean value for each input number (True if 0, False otherwise).
    """
    return [n == 0 for n in numbers]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to ensure no external inputs are needed.
    sample_data = [1, -5, 0, 3, 0, "invalid"]

    try:
        results = check_zeros(sample_data)
        
        # Print each result on a new line for clarity while handling non-integer inputs gracefully.
        for is_zero in results:
            print(is_zero)
            
    except Exception as e:
        # Graceful error handling for unexpected issues during processing.
        print(f"An error occurred: {e}")