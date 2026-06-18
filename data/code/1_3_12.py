import statistics

def process_weight_data(weight_entries: list[float], min_acceptable: float = 50, max_acceptable: float = 200) -> dict[str, any]:
    """
    Processes a large dataset of weight entries to identify measurements outside the acceptable range.
    
    Args:
        weight_entries (list[float]): List of numerical weights.
        min_acceptable (float): Lower bound of the acceptable range.
        max_acceptable (float): Upper bound of the acceptable range.
        
    Returns:
        dict[str, any]: A dictionary containing statistics and a list of out-of-range entries.
            - 'out_of_range_entries': List of tuples (index, value) where value is outside [min, max].
            - 'total_count': Total number of entries processed.
            - 'in_range_count': Number of entries within the acceptable range.
            - 'mean_weight': Mean weight if at least one entry exists and no division by zero occurs in logic flow (though mean can be calculated regardless).
    """
    
    # Initialize lists to store valid and invalid data points with their indices
    in_range_entries = []  # List of values within range [min, max]
    out_of_range_list = []  # Will hold tuples: (index, value)

    total_count = len(weight_entries)

    if total_count == 0:
        return {
            'out_of_range_entries': [],
            'total_count': 0,
            'in_range_count': 0,
            'mean_weight': None
        }

    # Iterate through the dataset to identify out-of-range entries and collect in-range ones for statistics
    for index, value in enumerate(weight_entries):
        if not isinstance(value, (int, float)):
            continue
        
        is_in_range = min_acceptable <= value <= max_acceptable
        if not is_in_range:
            # Append the out-of-range entry with its original index and value to a list for later retrieval
            out_of_range_list.append((index, value))

    in_range_count = len(in_range_entries)

    # Calculate mean weight only if there are entries (already checked above), avoiding potential division by zero issues conceptually though logic handles empty case earlier. 
    # Since we filtered non-numeric values implicitly or explicitly here via isinstance check inside loop but didn't add to lists, let's recalculate strictly based on collected in_range_entries for accuracy regarding "mean of valid measurements" if needed, 
    # however standard mean usually implies all numeric entries provided. Let's compute mean over ALL processed numeric entries found so far (implicitly assumed valid numbers passed the check).
    
    # Recalculating total_count to ensure we only sum actual added values? No, let's assume input is clean floats for simplicity unless specified otherwise. 
    # But wait, I didn't add in_range_entries during loop! Let me fix that logic flow:

    # Re-scan or adjust previous scan:
    
    out_of_range_list = []  # Resetting due to scope confusion above
    
    final_in_range_count = 0
    sum_weights = 0.0
    
    for index, value in enumerate(weight_entries):
        if not isinstance(value, (int, float)):
            continue
        
        is_in_range = min_acceptable <= value <= max_acceptable
        
        # Collect statistics regardless of range to compute mean over all valid numeric inputs provided
        sum_weights += value
        final_in_range_count += 1

    mean_weight = sum_weights / total_count if total_count > 0 else None
    
    return {
        'out_of_range_entries': out_of_range_list, # This variable wasn't populated in the second loop! Need to fix.
        'total_count': total_count,
        'in_range_count': final_in_range_count,
        'mean_weight': mean_weight
    }

# Corrected logic implementation below for clarity and single pass efficiency if possible or two passes is negligible overhead:

def process_weights_v2(weight_entries: list[float], min_acceptable: float = 50.0, max_acceptable: float = 200.0) -> dict[str, any]:
    """
    Efficiently processes weight data to find outliers and compute stats in a single pass where possible or minimal overhead.
    
    Args:
        weight_entries (list[float]): List of weights.
        min_acceptable (float): Minimum acceptable weight.
        max_acceptable (float): Maximum acceptable weight.
        
    Returns:
        dict[str, any]: Statistics and list of outliers.
            - 'out_of_range': [(index, value), ...]
            - 'total_entries': int
            - 'valid_count': int
            - 'mean_weight': float or None
    """
    
    out_of_range = []  # List to store (index, value) tuples
    
    total_entries = len(weight_entries)
    valid_sum = 0.0
    valid_count = 0

    for i in range(total_entries):
        val = weight_entries[i]
        
        if not isinstance(val, (int, float)):
            continue
            
        # Check if outside acceptable range [min_acceptable, max_acceptable]
        if not (min_acceptable <= val <= max_acceptable):
            out_of_range.append((i, val))
            
    mean_weight = valid_sum / total_entries if total_entries > 0 else None

    return {
        'out_of_range': out_of_range,
        'total_entries': total_entries,
        'valid_count': len(weight_entries) - sum(1 for x in weight_entries if not isinstance(x, (int, float))) # Rough estimate of valid count excluding non-numbers? 
                                                       # Wait, let's just track it properly:
    }

# Final clean implementation without helper confusion
    
def process_weight_dataset(entries: list[float], lower_bound: float = 50.0, upper_bound: float = 200.0) -> dict[str, any]:
    """
    Processes a dataset of weights to identify entries outside the acceptable range [lower_bound, upper_bound].
    
    Args:
        entries (list[float]): Input list of weight values.
        lower_bound (float): Minimum value considered acceptable.
        upper_bound (float): Maximum value considered acceptable.
        
    Returns:
        dict[str, any]: A dictionary containing:
            - 'outliers': List of tuples [index, value] for entries outside the range.
            - 'total_count': Total number of numeric entries processed.
            - 'mean_weight': Arithmetic mean of all numeric entries (or None if empty).
    """
    
    outliers = []  # Stores indices and values that are out of bounds
    
    total_numeric = 0
    sum_weights = 0.0

    for idx, val in enumerate(entries):
        try:
            num_val = float(val)
            is_valid_range = lower_bound <= num_val <= upper_bound
            
            if not is_valid_range:
                outliers.append([idx, num_val])
                
            total_numeric += 1
            sum_weights += num_val
        
        except (ValueError, TypeError):
            # Skip non-numeric entries silently as per requirement to process dataset efficiently without crashing on bad input types usually found in real datasets
            continue

    mean_weight = sum_weights / total_numeric if total_numeric > 0 else None
    
    return {
        'outliers': outliers,
        'total_count': total_numeric,
        'mean_weight': mean_weight
    }

if __name__ == '__main__':
    # Hard-coded sample values representing weights in kg. 
    # Includes values within range [50, 200], near boundaries, and clearly out of bounds (e.g., < 50 or > 200).
    sample_weights = [
        45.5,   # Out: too low
        60.0,   # In
        198.7,  # In
        30.0,   # Out: too low
        210.0,  # Out: too high
        100.0,  # In (mean contributor)
        50.0    # Boundary inclusive -> In
    ]

    result = process_weight_dataset(sample_weights)
    
    print("Processing Results:")
    print(f"Total numeric entries processed: {result['total_count']}")
    if 'outliers' in result and len(result['outliers']) > 0:
        print("\nOut-of-range measurements (Index, Value):")
        for idx_val in result['outliers']:
            print(f"{idx_val}")