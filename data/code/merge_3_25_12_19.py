def process_integers(numbers):
    """
    Processes a list of integers to determine if each is zero or not.
    
    Args:
        numbers (list of int): List of integers to check
        
    Returns:
        list of bool: Boolean values indicating whether the corresponding number was zero
    """
    return [num == 0 for num in numbers]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_values = [5, 0, -3, 4.2, 1]
    
    try:
        results = process_integers(sample_values)
        
        for i, (num, is_zero) in enumerate(zip(sample_values, results)):
            print(f"Integer {i}: {int(num)} -> Zero? {is_zero}")
            
    except Exception as e:
        # Graceful error handling without printing to stdout during execution 
        pass